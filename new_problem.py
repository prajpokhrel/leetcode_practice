# This is the auto-setup script for new LeetCode problems.

import os
import sys

TEMPLATE_SOLUTION = '''"""
Problem:
Link:
Difficulty:
"""

def solution(*args):
    pass


if __name__ == "__main__":
    print(solution())
'''

TEMPLATE_NOTES = '''# Problem Title

**Link**:  
**Difficulty**:  

## Approach

## Time Complexity

## Space Complexity

## Learnings
'''


def create_problem_folder(problem_number, problem_title, difficulty):
    folder_name = f"{problem_number.zfill(4)}-{problem_title}"
    path = os.path.join("problems", folder_name)

    if os.path.exists(path):
        print(f"Folder {path} already exists.")
        return

    os.makedirs(path)
    
    with open(os.path.join(path, "solution.py"), "w") as f:
        f.write(TEMPLATE_SOLUTION)

    with open(os.path.join(path, "notes.md"), "w") as f:
        f.write(TEMPLATE_NOTES)

    print(f"✅ Created folder: {path}")

    # title_display = problem_title.replace("-", " ").title()
    # leetcode_link = "None"
    # update_readme(problem_number, problem_title, title_display, difficulty, leetcode_link)

def update_readme(problem_number, problem_title, title_display, difficulty, link):
    readme_path = "README.md"
    row = f"| {int(problem_number)} | {title_display} | [Link]({link}) | {difficulty} | 🚧 In Progress |\n"

    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write("🧠 My LeetCode progress as I prepare for software engineering roles. Daily practice, notes, and solutions.\n\n")
            f.write("## Problems Tracker\n\n")
            f.write("| # | Title | Link | Difficulty | Status |\n")
            f.write("|---|-------|------|------------|--------|\n")

    # Check for duplicates
    with open(readme_path, "r") as f:
        if title_display in f.read():
            print(f"⚠️  Problem '{title_display}' already in README.md.")
            return

    with open(readme_path, "a") as f:
        f.write(row)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python new_problem.py <problem_number> <problem-title> <difficulty>")
        sys.exit(1)

    problem_number = sys.argv[1]
    problem_title = sys.argv[2]
    difficulty = sys.argv[3].capitalize()
    create_problem_folder(problem_number, problem_title, difficulty)
