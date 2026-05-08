def check_patterns(password):
    return {
        "length_ok": len(password) >= 8,
        "has_uppercase": any(char.isupper() for char in password),
        "has_lowercase": any(char.islower() for char in password),
        "has_number": any(char.isdigit() for char in password),
        "has_symbol": any(not char.isalnum() for char in password)
    }
