# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 1
- Student name: Moayed Mohamed Saleh
- Matric no: A24CS0017
- Group ID: n/a
- AI level: 1 
- Tools cited: OpenAI (2026). ChatGPT (GPT-6). Accessed 29 October 2026 from https://chatgpt.com/

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 29 October 2026
- Tool: OpenAI (2026). ChatGPT (GPT-6). https://chatgpt.com/
- Purpose: explain
- Prompt: "attached lab files + what exactly im supposed to do???"
- Output: explained the Lab 1 requirements, task sequence, repository structure, and required submission files.
- Verified by: compared the guidance with the Lab 1 student instructions.
- My change: used the explanation to understand the tasks and organize my workflow.
- Used in: Lab 1 preparation.

## Entry 2

- Date: 29 October 2026
- Tool: OpenAI (2026). ChatGPT (GPT-6). https://chatgpt.com/
- Purpose: debug
- Prompt: "explain y the error?" [(.venv) PS C:\Users\mwyd8\OneDrive\Desktop\University 47\SEMESTER 5\Programming For Bioinformatics\SECB3203_lab01_starter\lab01> pip install -r requirements.txt
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\mwyd8\OneDrive\Desktop\University 47\SEMESTER 5\Programming For Bioinformatics\SECB3203_lab01_starter\lab01\.venv\Scripts\pip.exe\__main__.py", line 4, in <module>
SyntaxError: source code string cannot contain null bytes]

- Output: Explained the null-byte SyntaxError in pip and suggested troubleshooting the virtual environment.

That means the problem is not your lecturer's code or requirements.txt. Python is encountering invalid null bytes while loading pip itself.

Since your project is inside OneDrive, file synchronization is one possible cause, but we can't confirm that.
Fix it step by step
We'll recreate only .venv, without touching any of your lecturer's files.
Step 1 — Deactivate your environment
Step 2 — Delete the corrupted environment
This deletes only the virtual environment, not your Python project.
Step 3 — Create a fresh environment
Step 4 — Activate it
Step 5 — Verify pip
Step 6 — Install the lecturer's requirements

- Verified by: recreated the virtual environment, installed the required packages successfully, and verified pip was working.
- My change: recreated the corrupted virtual environment and installed the dependencies again.
- Used in: T1 environment setup.

## Entry 3

- Date: 29 October 2026
- Tool: OpenAI (2026). ChatGPT (GPT-6). https://chatgpt.com/
- Purpose: explain
- Prompt: "pasted the readme template + is the linux/macos must??"
- Output: Explained why the README requires both Windows and Linux/macOS setup commands for reproducibility.
- Verified by: Checked the requirements in the lecturer's README template.
- My change: i didnt use it since i only used the windows terminal
- Used in: README.md, Setup section.

## Entry 4

- Date: 29 October 2026
- Tool: OpenAI (2026). ChatGPT (GPT-6). https://chatgpt.com/
- Purpose: explain
- Prompt: "gimme what should i do in readme?"
- Output: for README.md, keep the lecturer's original headings and replace the placeholders. Don't create a different README. 
1. Student information
At the top, fill in your name and matric number: 
2. Setup
This section must include both Windows and Linux/macOS, even though you only used Windows.

Under ## Setup, write that you used Windows PowerShell, then include:

Windows PowerShell (your actual setup)
3. Run
The lecturer requires the exact commands to run the tests, style checker, and environment report.
- Verified by: [Describe how you checked your README against the lecturer's template.]
- My change: [Describe the README sections you personally completed.]
- Used in: README.md.

4. What is in this repository 

5. What is not committed in github, and why


