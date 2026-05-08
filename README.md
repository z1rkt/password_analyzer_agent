# Password Strength Analyzer Agent

## Planned System and Goal

The system I plan to create is a Python program that checks how strong a password is.

The goal is to help users understand if their password is safe or not.

The program will look at things like how long the password is and what characters it uses. After that, it will give a score and some suggestions to improve it.

## AI / Agent-Based Approach

The system will use a simple agent-based approach.

The agent will:

- take a password from the user
- use different tools to check it
- combine the results
- show the final output

This is a rule-based AI system, because it makes decisions using simple conditions and rules.

## Tools Used in the System

The system will use these tools:

### Pattern Checker Tool

Checks password length and if it has uppercase letters, lowercase letters, numbers, or symbols.

### Scoring Tool

Gives a score based on the password strength.

### Suggestion Tool

Gives ideas on how to make the password better.

## Preliminary Programming Concepts

In this project I will use:

- Functions
- Classes
- Separate files / modules
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


After the project structure, also add this small part so it clearly covers Step 2 requirements:

```markdown
## Programming Concepts Used

In the implementation I used functions, class, modules, if/else statements, loops, lists, dictionaries, input and output.

Functions are used for checking the password, calculating the score, and giving suggestions.

A class is used in agent.py. The PasswordAgent class controls the workflow.

Modules are used because the code is separated into different files.

If/else statements are used to decide if the password is weak, medium, or strong.

Loops are used to print the checks and suggestions.

Lists are used to store suggestions.

Dictionaries are used to store password check results.

## Tool Integration

The agent uses three tools during execution.

The Pattern Checker Tool checks the password.

The Scoring Tool calculates the score.

The Suggestion Tool gives improvement suggestions.

The basic workflow is:

User enters password → Agent checks password → Tools return results → Program shows score and suggestions.

## Current Progress

The basic version of the system works.

It can take user input, use tools, calculate a score, and give suggestions.

Testing and deployment preparation will be added later.
