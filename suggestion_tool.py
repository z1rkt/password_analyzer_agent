def give_suggestions(results):
    suggestions = []

    if not results["length_ok"]:
        suggestions.append("Make the password at least 8 characters long.")

    if not results["has_uppercase"]:
        suggestions.append("Add an uppercase letter.")

    if not results["has_lowercase"]:
        suggestions.append("Add a lowercase letter.")

    if not results["has_number"]:
        suggestions.append("Add a number.")

    if not results["has_symbol"]:
        suggestions.append("Add a special symbol.")

    if len(suggestions) == 0:
        suggestions.append("Password looks strong.")

    return suggestions
