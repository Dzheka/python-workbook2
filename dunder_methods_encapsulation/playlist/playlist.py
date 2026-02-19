class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add(self, title, duration):
        self.songs.append({"title": title, "duration": duration})

    def __len__(self):
        return len(self.songs)

    def __contains__(self, title):
        return any(s["title"] == title for s in self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __add__(self, other):
        merged = Playlist(f"{self.name} + {other.name}")
        merged.songs = self.songs + other.songs
        return merged

    def __eq__(self, other):
        return self.songs == other.songs

    def __str__(self):
        total = sum(s["duration"] for s in self.songs)
        mins, secs = divmod(total, 60)
        lines = [f"\U0001f3a7 {self.name} ({len(self.songs)} songs, {mins}:{secs:02d})"]
        for i, s in enumerate(self.songs, 1):
            m, sec = divmod(s["duration"], 60)
            lines.append(f"  {i}. {s['title']} ({m}:{sec:02d})")
        return "\n".join(lines)


rock = Playlist("Rock")
rock.add("Bohemian Rhapsody", 354)
rock.add("Stairway to Heaven", 482)

pop = Playlist("Pop")
pop.add("Blinding Lights", 200)

print(len(rock))
print("Bohemian Rhapsody" in rock)
print(rock[0])

merged = rock + pop
print(len(merged))
print(merged)
