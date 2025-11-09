
"""
Step 4 — Add Tkinter GUI (2-player). CLI modes unchanged.In here I add a normal GUI version of this game.

"""

from typing import Dict, List, Optional, Tuple

Board = List[str]
WIN_LINES: Tuple[Tuple[int, int, int], ...] = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)

def draw_board(b: Board) -> None:
    def cell(i: int) -> str: return b[i] if b[i] != " " else str(i + 1)
    print(
        f"\n {cell(0)} | {cell(1)} | {cell(2)}\n"
        f"---+---+---\n"
        f" {cell(3)} | {cell(4)} | {cell(5)}\n"
        f"---+---+---\n"
        f" {cell(6)} | {cell(7)} | {cell(8)}\n"
    )

def winner(b: Board) -> Optional[str]:
    for a, c, d in WIN_LINES:
        if b[a] != " " and b[a] == b[c] == b[d]:
            return b[a]
    return None

def empty_squares(b: Board) -> List[int]:
    return [i for i, v in enumerate(b) if v == " "]

def full(b: Board) -> bool:
    return all(x != " " for x in b)

def try_win_or_block(b: Board, me: str, opp: str) -> Optional[int]:
    for i in empty_squares(b):
        b[i] = me
        if winner(b) == me:
            b[i] = " "
            return i
        b[i] = " "
    for i in empty_squares(b):
        b[i] = opp
        if winner(b) == opp:
            b[i] = " "
            return i
        b[i] = " "
    return None

def best_move(b: Board, me: str, opp: str) -> int:
    move = try_win_or_block(b, me, opp)
    if move is not None:
        return move
    empties = empty_squares(b)
    if 4 in empties:
        return 4
    for i in (0, 2, 6, 8):
        if i in empties:
            return i
    return empties[0]

def cli_two_player() -> None:
    board: Board = [" "] * 9
    turn = "X"
    print("Two-player Tic-Tac-Toe Championship.Organised by keele university. Enter 1-9.")
    while True:
        draw_board(board)
        move = input(f"Player {turn}, move (1-9): ").strip()
        if not move.isdigit():
            print("Please enter 1-9."); continue
        idx = int(move) - 1
        if idx not in range(9) or board[idx] != " ":
            print("Invalid move."); continue
        board[idx] = turn
        w = winner(board)
        if w or full(board):
            draw_board(board)
            print(f"Player {w} wins!Best wishes from keele university!!" if w else "It's a draw.Try again !!!")
            break
        turn = "O" if turn == "X" else "X"

def cli_vs_ai_loop() -> None:
    human, ai = "X", "O"
    scores: Dict[str, int] = {"you": 0, "ai": 0, "draws": 0}
    print("Tic-Tac-Toe vs AI. You are X.")
    while True:
        board: Board = [" "] * 9
        turn = "X"
        while True:
            draw_board(board)
            if turn == human:
                move = input("Your move (1-9): ").strip()
                if not move.isdigit():
                    print("Please enter 1-9."); continue
                idx = int(move) - 1
                if idx not in range(9) or board[idx] != " ":
                    print("Invalid move."); continue
            else:
                idx = best_move(board, ai, human)
                print(f"AI plays {idx + 1}")
            board[idx] = turn
            w = winner(board)
            if w or full(board):
                draw_board(board)
                if w == human:
                    print("You win!Best wishes from keele university!!"); scores["you"] += 1
                elif w == ai:
                    print("AI wins!"); scores["ai"] += 1
                else:
                    print("It's a draw."); scores["draws"] += 1
                print(f"Score — You: {scores['you']} | AI: {scores['ai']} | Draws: {scores['draws']}")
                break
            turn = "O" if turn == "X" else "X"
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!Keep continue...keele university")
            break


def gui_two_player() -> None:
    try:
        import tkinter as tk
    except Exception as e:
        print("Tkinter not available:", e); return

    class App:
        def __init__(self, root: "tk.Tk") -> None:
            self.root = root
            self.root.title("Tic-Tac-Toe (2-player)")
            self.board: Board = [" "] * 9
            self.turn = "X"
            self.btns: List["tk.Button"] = []
            self.status = tk.StringVar(value="Player X's turn")
            self.build()

        def build(self) -> None:
            top = tk.Frame(self.root, padx=8, pady=8); top.pack()
            grid = tk.Frame(top); grid.grid(row=0, column=0, columnspan=3)
            for i in range(9):
                b = tk.Button(grid, text=" ", width=5, height=2, font=("Arial", 20),
                              command=lambda i=i: self.play(i))
                b.grid(row=i//3, column=i%3, padx=4, pady=4)
                self.btns.append(b)
            tk.Button(top, text="New Round", command=self.reset).grid(row=1, column=0, pady=(8,0))
            tk.Label(top, textvariable=self.status, font=("Arial", 12)).grid(row=2, column=0, columnspan=3, pady=(6,0))

        def play(self, i: int) -> None:
            if self.board[i] != " ":
                return
            self.board[i] = self.turn
            self.btns[i]["text"] = self.turn
            w = winner(self.board)
            if w:
                self.status.set(f"Player {w} wins!Best of luck from keele uni"); self.disable()
            elif full(self.board):
                self.status.set("Draw! Try again!!"); self.disable()
            else:
                self.turn = "O" if self.turn == "X" else "X"
                self.status.set(f"Player {self.turn}'s turn")

        def reset(self) -> None:
            self.board = [" "] * 9
            for b in self.btns: b.config(text=" ", state="normal")
            self.turn = "X"; self.status.set("Player X's turn")

        def disable(self) -> None:
            for b in self.btns: b.config(state="disabled")

    root = tk.Tk()
    App(root)
    root.mainloop()

def main() -> None:
    print("Choose mode Keele university Tic tac Toe Championship:\n  1) CLI 2-player\n  2) CLI vs AI (scores & replay)\n  3) GUI 2-player")
    choice = input("Enter 1/2/3: ").strip()
    if choice == "2":
        cli_vs_ai_loop()
    elif choice == "3":
        gui_two_player()
    else:
        cli_two_player()

if __name__ == "__main__":
    try:
        main()
    finally:
        try:
            input("\nPress Enter to exit...bye bye!!")
        except EOFError:
            pass