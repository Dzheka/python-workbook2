def remove_duplicate_letters(text: str) -> str:
    """your code"""
    seen = set()
    result = []

    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return "".join(result)
