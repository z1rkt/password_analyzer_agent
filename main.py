from agent import PasswordAgent

password = input("Enter password to check: ")

agent = PasswordAgent()
result = agent.analyze_password(password)

print("\nPassword strength:", result["strength"])
print("Score:", result["score"], "/ 5")

print("\nChecks:")
for check, value in result["results"].items():
    print(check, ":", value)

print("\nSuggestions:")
for suggestion in result["suggestions"]:
    print("-", suggestion)
