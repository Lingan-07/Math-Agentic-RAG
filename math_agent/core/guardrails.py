import re

def validate_math_query(query: str) -> bool:
    """
    Guardrail: Allow only math-related queries.
    """
    math_keywords = ["solve", "calculate", "integrate", "differentiate", "equation", "formula", "math", "algebra", "geometry", "trigonometry", "calculus", "matrix", "statistics", "probability"]
    if any(word in query.lower() for word in math_keywords):
        return True

    return bool(re.search(r"[\d\+\-\*/\^\=\(\)]", query))