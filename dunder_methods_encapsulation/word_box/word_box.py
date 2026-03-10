class WordBox:
    def __init__(self):
        self.words = []

    def add(self, word):
        word = word.lower()
        self.words.append(word.lower())

    def __len__(self):
        return  len(self.words)

    def __contains__(self, word: str):
        for s_word in self.words:
            if s_word.lower() == word.lower():
                return True
        return False

    def __str__(self):
        word_string = ", ".join(self.words)
        return f"WordBox({len(self.words)} words: {word_string})"





box = WordBox()
box.add("Hello")
box.add("World")
box.add("Python")

print(len(box))          # 3
print("hello" in box)    # True
print("WORLD" in box)    # True
print("Java" in box)     # False
print(box)               # WordBox(3 words: hello, world, python)