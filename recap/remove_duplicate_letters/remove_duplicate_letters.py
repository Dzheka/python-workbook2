def remove_duplicate_letters(text: str) -> str:
    res = []
    for i in range (len(text)):
        let = text[i]
        if let not in res:
            res.append(let)
    res = "".join(res)
    return res




if __name__ == "__main__":
    print(remove_duplicate_letters("hello"))  # "helo"
    print(remove_duplicate_letters("mississippi"))  # "misp"
    print(remove_duplicate_letters("abcabc"))  # "abc"
    print(remove_duplicate_letters("AaAaBb"))  # "AaBb"
    print(remove_duplicate_letters(""))  # ""
