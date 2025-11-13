_______________________________________
✅ Tic-Tac-Toe Game — CSC-44102 Assessment 2
________________________________________
✅ Overview
A simple Tic-Tac-Toe game built in Python with CLI and Tkinter GUI, developed in incremental steps to demonstrate Git workflow, branching, merging, and software engineering best practices.
________________________________________
▶ How to Run
python tictactoe.py
Ensure you have Python 3 installed.\ Tkinter is included by default on most systems. On Linux, install with:
sudo apt-get install python3-tk
________________________________________
🎮 Controls
CLI Modes:
•	Enter 1–9 → Place your mark in the corresponding cell.
•	Replay option in AI mode → Type y or n.
GUI Modes:
•	Click a square → Place your mark.
•	New Round → Reset the board.
•	Mode toggle → Switch between Human vs Human and Human vs AI.
________________________________________
✨ Features
•	Step 1: CLI 2-player game.
•	Step 2: CLI Human vs AI (simple heuristic).
•	Step 3: Scoreboard & replay in CLI AI mode.
•	Step 4: Basic Tkinter GUI for 2-player.
•	Step 5: GUI with Human vs AI + scoreboard.
________________________________________
📂 Project Structure
.
├── tictactoe.py    # Single file containing all modes (CLI + GUI)
├── README.md       # Project documentation
________________________________________
🔀 Git Workflow Summary
✅ Branches:
•	main → Starts with CLI 2-player game.
•	feature-ai → Adds AI and scoreboard.
•	feature-gui → Adds GUI and integrates AI.
✅ Commits:
•	Step 1: feat: Step 1 — Add simple 2-player terminal game
•	Step 2: feat(ai): Step 2 — Add single-player vs AI (CLI)
•	Step 3: feat(ai): Step 3 — Add scoreboard & replay to CLI vs AI
•	Step 4: feat(gui): Step 4 — Add basic Tkinter GUI (2-player)
•	Step 5: feat(gui): Step 5 — Integrate AI + scoreboard in GUI
✅ Merges:
•	Merge #1: feature-ai → feature-gui (non-fast-forward, visible in history)
•	Merge #2: feature-gui → main (fast-forward after final integration)
________________________________________
✅ How It Works
•	CLI 2-player: Players alternate entering numbers (1–9).
•	CLI vs AI: AI uses a simple strategy (win → block → center → corners → sides).
•	GUI: Interactive board with buttons, mode toggle, and scoreboard.
________________________________________
🖼 Commit History Example
✔ Merge commits visible for feature-ai and feature-gui. 
✔ Informative commit messages for each step.
________________________________________
🤖 GenAI Acknowledgment
I acknowledge the use of Microsoft Copilot (M365 Copilot) to create parts of the code in this project.
________________________________________
👤 Author
Md Shoab Siddiq. Email: [y5c83@students.keele.ac.uk]
________________________________________
✅ Why This README Stands Out:
✔ Uses icons for sections (✅ ▶ 🎮 ✨ 📂 🔀 🤖 👤).\ ✔ Includes How to Run, Controls, Features, Git Workflow, and Acknowledgment.\ ✔ Matches the style of your example but customized for Tic-Tac-Toe.


