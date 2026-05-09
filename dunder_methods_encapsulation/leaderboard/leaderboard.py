class Leaderboard:
    def __init__(self):
        self.entries = []

    def add(self, name, score):
        self.entries.append({"name": name, "score": score})
        self.entries.sort(key=lambda e: e["score"], reverse=True)

    def __getitem__(self, index):
        return self.entries[index]

    def __len__(self):
       return len(self.entries)

    def __contains__(self, name):
        return any(e["name"] == name for e in self.entries)

    def __str__(self):
        first = ["🏆 Leaderboard"]
        for i, j in enumerate(self.entries, start=1):
            first.append(f"{i}. {j['name']} - {j['score']}")
        return "\n".join(first)

lb = Leaderboard()
lb.add("Alice", 300)
lb.add("Bob", 500)
lb.add("Charlie", 150)

print(len(lb))        # 3
print(lb[0])          # {'name': 'Bob', 'score': 500}
print(lb[1])          # {'name': 'Alice', 'score': 300}
print("Alice" in lb)  # True
print("Dave" in lb)   # False

print(lb)
# 🏆 Leaderboard:
#  1. Bob — 500
#  2. Alice — 300
#  3. Charlie — 150