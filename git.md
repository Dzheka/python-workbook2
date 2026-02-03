Open your terminal/command prompt.

Create a folder and enter it:

Bash
mkdir git_survival_lab
cd git_survival_lab
Create a file named main.py and write: print("Hello Git!")

Initialize Git: git init

Check Status: git status (Notice the file is red).

Save it: ```bash git add main.py git commit -m "Initial commit: starting the lab"


Step 2: Building History
Add a new function to main.py:

Python
def greet(name):
    return f"Hello, {name}!"
Save and commit: git add . then git commit -m "Feat: added greet function"

Add another change (e.g., a math function) and commit it: git commit -m "Feat: added math logic"

Run git log --oneline to see your progress.

Step 3: The Emergency (Restore)
The Accident: Delete all the code inside main.py and save the empty file.

The Panic: Try to run it. It does nothing!

The Rescue: Run git status to see the modification.

The Time Travel:

Bash
git restore main.py
Check your file. It’s back!

Step 4: The .gitignore
Create a "trash" file that we don't want in our history: secrets.txt.

Run git status. Notice Git wants to track secrets.txt.

Create a new file named .gitignore.

Inside .gitignore, simply type:

Plaintext
secrets.txt
__pycache__/
Run git status again. secrets.txt is now invisible to Git!

Commit your ignore file: git add .gitignore and git commit -m "Docs: added gitignore"

✅ Final Check (Submission)
To finish the lesson, show your teacher the output of:

Bash
git log --oneline
You should have at least 4 commits.
