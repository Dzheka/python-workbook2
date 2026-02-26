class WordBox:
    def __init__(self, words=None):
        self.words = words

    def add(self, word):
        return self.words.append(word.lower())

    def __len__(self):
        return len(self.words)
    
    def __contains__(self, word):
        return word.lower() in self.words
    
    def __str__(self):
        return f"WordBox({len(self.words)} words: {self.words})"
    
box = WordBox()
box.add("Hello")
box.add("World")
box.add("Python")

print(len(box))          # 3
print("hello" in box)    # True
print("WORLD" in box)    # True
print("Java" in box)     # False
print(box)               # WordBox(3 words: hello, world, python)