def predict_resume_score(score):
    """Map a numeric resume score to a qualitative assessment.

    Accepts ints, floats, and numeric strings in the range 0-100. Invalid or
    out-of-range values raise ValueError so callers can correct the input.
    """
    if isinstance(score, bool):
        raise ValueError("score must be a numeric value between 0 and 100")

    if isinstance(score, str):
        score = score.strip()
        if not score:
            raise ValueError("score cannot be empty")
        try:
            score = float(score)
        except ValueError as exc:
            raise ValueError(
                "score must be a numeric value between 0 and 100"
            ) from exc

    if not isinstance(score, (int, float)):
        raise TypeError("score must be a number or numeric string")

    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")

    if score >= 80:
        return "Excellent"
    if score >= 60:
        return "Good"
    if score >= 40:
        return "Average"
    return "Needs Improvement"