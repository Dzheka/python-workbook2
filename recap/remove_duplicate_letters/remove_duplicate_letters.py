def remove_duplicate_letters(text: str) -> str:
    seen = []
    result = ""
    for char in text:
        if char not in seen:
            seen.append(char)
            result += char
    return result


if __name__ == "__main__":
    print(remove_duplicate_letters("hello"))
    print(remove_duplicate_letters("mississippi"))
    print(remove_duplicate_letters("abcabc"))
    print(remove_duplicate_letters("AaAaBb"))
    print(remove_duplicate_letters(""))
