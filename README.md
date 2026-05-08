# Password Strength Analyzer Agent

- Planned System and Goal
The system I plan to create is a Python program that checks how strong a password is.  
The goal is to help users understand if their password is safe or not.

The program will look at things like how long the password is and what characters it uses. After that, it will give a score and some suggestions to improve it.

- AI / Agent-Based Approach
The system will use a simple agent-based approach.

The agent will:
- take a password from the user,
- use different tools to check it,
- combine the results,
- and show the final output.

This is a rule-based AI system, because it makes decisions using simple conditions and rules.

- Tools Used in the System
The system will use these tools:

- Pattern Checker Tool  
  Checks password length and if it has uppercase letters, numbers, or symbols.

- Scoring Tool  
  Gives a score based on the password strength.

- Suggestion Tool  
  Gives ideas on how to make the password better.

- Preliminary Programming Concepts
In this project I will use:

- Functions  
- Classes  
- Separate files (modules)  
- If/else statements  
- Loops  
- Lists and dictionaries  
- Input and output

## Current Project Status

The Password Strength Analyzer Agent is now partly implemented in Python.

The system can take a password from the user, check the password with different tools, calculate a score, and give suggestions for improvement.

The project is still in development, but the basic workflow is working.

## Project Structure

```text
password_strength_agent/
│
├── main.py
├── agent.py
├── pattern_checker.py
├── scoring_tool.py
├── suggestion_tool.py
└── README.md
