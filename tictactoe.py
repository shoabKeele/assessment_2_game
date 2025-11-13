# I acknowledge the use of AI for help and generate idea and develop the game..
"""
Step 5 — GUI with Human-vs-AI or Human-vs-Human + scoreboard.This is the final version of the game.

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
    print("Two-player Tic-Tac-Toe. Enter 1-9.")
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
            print(f"Player {w} wins!best wishes from keele university!!" if w else "It's a draw.")
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
                    print("You win!best wishes from Keele University!!"); scores["you"] += 1
                elif w == ai:
                    print("AI wins!"); scores["ai"] += 1
                else:
                    print("It's a draw.OH!no!! try again!!"); scores["draws"] += 1
                print(f"Score — You: {scores['you']} | AI: {scores['ai']} | Draws: {scores['draws']}")
                break
            turn = "O" if turn == "X" else "X"
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break


def gui() -> None:
    try:
        import tkinter as tk
    except Exception as e:
        print("Tkinter not available:", e); return

    class App:
        def __init__(self, root: "tk.Tk") -> None:
            self.root = root
            self.root.title("Tic-Tac-Toe (GUI)")
            self.board: Board = [" "] * 9
            self.turn = "X"
            self.btns: List["tk.Button"] = []
            self.mode = tk.StringVar(value="PvAI")  # PvAI or PvP
            self.status = tk.StringVar(value="Your turn (X)")
            self.scores: Dict[str, int] = {"X": 0, "O": 0, "draws": 0}
            self.build()
            self.update_score()

        def build(self) -> None:
            top = tk.Frame(self.root, padx=8, pady=8); top.pack()

            modef = tk.Frame(top); modef.grid(row=0, column=0, columnspan=3, pady=(0,6))
            tk.Label(modef, text="Mode:").pack(side=tk.LEFT)
            tk.Radiobutton(modef, text="Human vs AI", variable=self.mode, value="PvAI",
                           command=self.reset).pack(side=tk.LEFT, padx=4)
            tk.Radiobutton(modef, text="Human vs Human", variable=self.mode, value="PvP",
                           command=self.reset).pack(side=tk.LEFT, padx=4)

            grid = tk.Frame(top); grid.grid(row=1, column=0, columnspan=3)
            for i in range(9):
                b = tk.Button(grid, text=" ", width=5, height=2, font=("Arial", 20),
                              command=lambda i=i: self.play(i))
                b.grid(row=i//3, column=i%3, padx=4, pady=4)
                self.btns.append(b)

            ctl = tk.Frame(top); ctl.grid(row=2, column=0, columnspan=3, pady=(6,0))
            tk.Button(ctl, text="New Round", command=self.reset).pack(side=tk.LEFT, padx=4)
            self.score_lbl = tk.Label(ctl, text="", font=("Arial", 12))
            self.score_lbl.pack(side=tk.LEFT, padx=10)

            tk.Label(top, textvariable=self.status, font=("Arial", 12)).grid(row=3, column=0, columnspan=3, pady=(6,0))

        def update_score(self) -> None:
            self.score_lbl.config(text=f"Score — X: {self.scores['X']} | O: {self.scores['O']} | Draws: {self.scores['draws']}")

        def reset(self) -> None:
            self.board = [" "] * 9
            for b in self.btns: b.config(text=" ", state="normal")
            self.turn = "X"
            self.status.set("Your turn (X)" if self.mode.get() == "PvAI" else "Player X's turn")

        def play(self, i: int) -> None:
            if self.board[i] != " " or self.game_over():
                return
            self.place(i, self.turn)
            if self.end_if_over(): return
            self.turn = "O" if self.turn == "X" else "X"

            if self.mode.get() == "PvAI" and self.turn == "O":
                self.root.after(150, self.ai_move)
            else:
                self.status.set(f"Player {self.turn}'s turn")

        def ai_move(self) -> None:
            if self.game_over(): return
            i = best_move(self.board, "O", "X")
            self.place(i, "O")
            self.end_if_over()
            self.turn = "X"
            if not self.game_over():
                self.status.set("Your turn (X)")

        def place(self, i: int, sym: str) -> None:
            self.board[i] = sym
            self.btns[i].config(text=sym)

        def end_if_over(self) -> bool:
            w = winner(self.board)
            if w or full(self.board):
                for b in self.btns: b.config(state="disabled")
                if w:
                    msg = ("You win!Best wishes from keele university!" if self.mode.get() == "PvAI" and w == "X"
                           else "AI wins!Best wishes from keele university!" if self.mode.get() == "PvAI" and w == "O"
                           else f"Player {w} wins!best wishes from Keele University!")
                    self.status.set(msg)
                    self.scores[w] += 1
                else:
                    self.status.set("Draw!")
                    self.scores["draws"] += 1
                self.update_score()
                return True
            return False

        def game_over(self) -> bool:
            return winner(self.board) is not None or full(self.board)

    root = tk.Tk()
    App(root)
    root.mainloop()

def main() -> None:
    print("Choose mode keele University Tic tac toe championship:\n  1) CLI 2-player\n  2) CLI vs AI (scores & replay)\n  3) GUI (PersonvPerson / PvAI + scoreboard)")
    choice = input("Enter 1/2/3: ").strip()
    if choice == "2":
        cli_vs_ai_loop()
    elif choice == "3":
        gui()
    else:
        cli_two_player()

if __name__ == "__main__":
    try:
        main()
    finally:
        try:
            input("\nPress Enter to exit...")
        except EOFError:
            pass