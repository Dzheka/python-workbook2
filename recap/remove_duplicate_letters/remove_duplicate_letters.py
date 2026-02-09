def remove_duplicate_letters(text: str) -> str:
    st = {}
    unique = ""

    for letter in text:
        if letter not in st:
            st[letter] = 1
            unique = unique + letter

    return  unique


if __name__ == "__main__":
    print(remove_duplicate_letters("hello"))  # "helo"
    print(remove_duplicate_letters("mississippi"))  # "misp"
    print(remove_duplicate_letters("abcabc"))  # "abc"
    print(remove_duplicate_letters("AaAaBb"))  # "AaBb"
    print(remove_duplicate_letters(""))  # ""
