class Leaderboard:
    def __init__(self):
        self.entries = []

    def add(self, name, score):
        self.entries.append({"name": name, "score": score})
        self.entries.sort(key=lambda x: x["score"], reverse=True)

    def __getitem__(self, index):
        return self.entries[index]

    def __len__(self):
        return len(self.entries)

    def __contains__(self, name):
        return any(entry["name"] == name for entry in self.entries)

    def __str__(self):
        lines = ["🏆 Leaderboard:"]
        for i, entry in enumerate(self.entries, start=1):
            lines.append(f" {i}. {entry['name']} — {entry['score']}")
        return "\n".join(lines)
