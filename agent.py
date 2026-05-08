from pattern_checker import check_patterns
from scoring_tool import calculate_score
from suggestion_tool import give_suggestions

class PasswordAgent:
    def analyze_password(self, password):
        results = check_patterns(password)
        score = calculate_score(results)
        suggestions = give_suggestions(results)

        if score <= 2:
            strength = "Weak"
        elif score <= 4:
            strength = "Medium"
        else:
            strength = "Strong"

        return {
            "score": score,
            "strength": strength,
            "results": results,
            "suggestions": suggestions
        }
