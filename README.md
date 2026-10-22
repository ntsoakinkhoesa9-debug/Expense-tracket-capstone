# Expense Tracker - UJ Capstone
Flet-based expense tracker built for UJ Capstone Project.

## Features
- Add, view expenses
- Model-View separation (Expense class)
- JSON persistence with empty-file handling
- High contrast UI (DeepPurple theme, large buttons)

## How to Run
pip install -r requirements.txt
flet run main.py

## Files
- main.py: UI and app logic
- models.py: Data model (for modularity)
- requirements.txt: Dependencies
- expenses.json: Storage (auto-created)

## Assessment Fixes
- Q33: Improved contrast and button size 400x50
- Fixed empty JSON file crash with os.stat check
- Modular code structure

Student: ntsoakinkhoesa
University of Johannesburg - 2025 Capstone
