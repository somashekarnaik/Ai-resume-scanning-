def predict_resume_score(
    score
):

    if score >= 80:

        return "Excellent"

    elif score >= 60:

        return "Good"

    elif score >= 40:

        return "Average"

    else:

        return "Needs Improvement"