def calculate_score(results):
    score = 0

    for value in results.values():
        if value == True:
            score += 1

    return score
