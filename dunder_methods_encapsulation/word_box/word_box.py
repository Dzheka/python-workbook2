class WordBox:
    def __init__(self):
        self.words = []

    def add(self, word):
        self.words.append(word.lower())

    def __len__(self):
        return len(self.words)

    def __contains__(self, word):
        return word.lower() in self.words

    def __str__(self):
        return f"WordBox({len(self)} words: {', '.join(self.words)})"
