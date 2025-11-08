# I acknowledge the use of AI for help and generate idea and develop the game. 
"""
Step 1 — Two-player terminal Tic-Tac-Toe where the game run only terminal using terminal or windows powershell for run this game.

"""

from typing import List, Optional, Tuple

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

def full(b: Board) -> bool:
    return all(x != " " for x in b)

def cli_two_player() -> None:
    board: Board = [" "] * 9
    turn = "X"
    print("Two-player Tic-Tac-Toe championship at Keele University. Enter a number (1-9) to place your mark.")
    while True:
        draw_board(board)
        move = input(f"Player {turn}, your move (1-9): ").strip()
        if not move.isdigit():
            print("Please enter a number 1-9.")
            continue
        idx = int(move) - 1
        if idx not in range(9) or board[idx] != " ":
            print("Invalid move. Try again.Don't loss hope!")
            continue
        board[idx] = turn

        w = winner(board)
        if w:
            draw_board(board)
            print(f"Player {w} wins! the Keele University Championship.hurry!!!")
            break
        if full(board):
            draw_board(board)
            print("It's a draw.")
            break

        turn = "O" if turn == "X" else "X"

def main() -> None:
    cli_two_player()

if __name__ == "__main__":
    try:
        main()
    finally:
        
        try:
            input("\nPress Enter to exit the game!!!bye bye...")
        except EOFError:
            pass