
"""
Step 3 — Add scoreboard + replay to CLI Human-vs-AI.In here I  add multiple time play and also add  scoreboard in AI mode.
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

# --- AI (same heuristic) ---
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

# --- Modes ---
def cli_two_player() -> None:
    board: Board = [" "] * 9
    turn = "X"
    print("Two-player Keel University Tic-Tac-Toe championship. Enter 1-9.")
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
            print(f"Player {w} wins!" if w else "It's a draw.")
            break
        turn = "O" if turn == "X" else "X"

def cli_vs_ai_loop() -> None:
    human, ai = "X", "O"
    scores: Dict[str, int] = {"you": 0, "ai": 0, "draws": 0}
    print("Tic-Tac-Toe vs AI organised by keele university. You are X.")
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
                    print("You win!"); scores["you"] += 1
                elif w == ai:
                    print("AI wins!"); scores["ai"] += 1
                else:
                    print("It's a draw."); scores["draws"] += 1
                print(f"Score — You: {scores['you']} | AI: {scores['ai']} | Draws: {scores['draws']}")
                break
            turn = "O" if turn == "X" else "X"
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!Best wishes from keele university!!")
            break

def main() -> None:
    print("Choose mode:\n  1) CLI 2-player\n  2) CLI vs AI (scores & replay)")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "2":
        cli_vs_ai_loop()
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