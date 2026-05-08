Password Strength Analyzer Agent
Planned System and Goal

The system I plan to create is a Python program that checks how strong a password is.

The goal is to help users understand if their password is safe or not.

The program will look at things like how long the password is and what characters it uses. After that, it will give a score and some suggestions to improve it.

AI / Agent-Based Approach

The system will use a simple agent-based approach.

The agent will:

take a password from the user
use different tools to check it
combine the results
show the final output

This is a rule-based AI system, because it makes decisions using simple conditions and rules.

Tools Used in the System

The system will use these tools:

Pattern Checker Tool

Checks password length and if it has uppercase letters, lowercase letters, numbers, or symbols.

Scoring Tool

Gives a score based on the password strength.

Suggestion Tool

Gives ideas on how to make the password better.

Preliminary Programming Concepts

In this project I will use:

Functions
Classes
Separate files / modules
If/else statements
Loops
Lists and dictionaries
Input and output
Current Project Status

The Password Strength Analyzer Agent is now partly implemented in Python.

The system can take a password from the user, check the password with different tools, calculate a score, and give suggestions for improvement.

The project is still in development, but the basic workflow is working.

Project Structure
password_strength_agent/
│
├── main.py
├── agent.py
├── pattern_checker.py
├── scoring_tool.py
├── suggestion_tool.py
└── README.md
Programming Concepts Used

In the implementation I used:

functions
class
modules
if/else statements
loops
lists
dictionaries
input and output
string methods

Functions are used in the tool files. For example, one function checks the password, one function calculates the score, and one function gives suggestions.

A class is used in agent.py. The PasswordAgent class controls the workflow and connects the tools together.

Modules are used because the code is separated into different Python files.

If/else statements are used to decide if the password is weak, medium, or strong.

Loops are used to print the checks and suggestions.

Lists are used to store suggestions.

Dictionaries are used to store the password check results.

Input and output are used so the user can enter a password and see the result.

String methods are used to check characters in the password.

Tool Integration

The agent uses three tools during execution.

The Pattern Checker Tool checks the password length, uppercase letters, lowercase letters, numbers, and symbols.

The Scoring Tool takes the pattern checker results and calculates a score.

The Suggestion Tool checks what is missing and gives advice to improve the password.

The workflow is:

User enters password
PasswordAgent receives password
Pattern Checker Tool checks password
Scoring Tool calculates score
Suggestion Tool gives suggestions
Program shows final result
How to Run

Run the program in the terminal:

python main.py

Then enter a password when asked.

Example Run

Input:

123

Output:

Password strength: Weak
Score: 2 / 5

Suggestions:
- Make the password at least 8 characters long.
- Add an uppercase letter.
- Add a special symbol.
Current Progress

The basic version of the system works.

It can accept user input, use tools, calculate a score, and give suggestions.

Testing and deployment preparation will be added later.
