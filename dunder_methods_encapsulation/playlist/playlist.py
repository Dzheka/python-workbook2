class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []

    def add(self,title,duration):
        songs = {
            "title": title,
            "duration": duration
        }
        self.songs.append(songs)


    def __len__(self):
        return len(self.songs)

    def __contains__(self, title):
        for song in self.songs:
            if song["title"] == title:
                return True
        return False


    def __getitem__(self, index):
        return self.songs[index]


    def __add__(self, other):
        new = Playlist(f"{self.name} + {other.name}")
        new.songs = self.songs + other.songs
        return new


    def __eq__(self, other):
        return self.songs == other.songs


    @staticmethod
    def _fmt(seconds):
        return f"{seconds // 60}:{seconds % 60:02d}"


    def __str__(self):
        total = sum(s["duration"] for s in self.songs)
        lines = [f"🎧 {self.name} ({len(self)} songs, {self._fmt(total)})"]
        for i, s in enumerate(self.songs, 1):
            lines.append(f"  {i}. {s['title']} ({self._fmt(s['duration'])})")
        return "\n".join(lines)



rock = Playlist("Rock")
rock.add("Bohemian Rhapsody", 354)
rock.add("Stairway to Heaven", 482)

pop = Playlist("Pop")
pop.add("Blinding Lights", 200)

print(len(rock))                    # 2
print("Bohemian Rhapsody" in rock)  # True
print(rock[0])                      # {'title': 'Bohemian Rhapsody', 'duration': 354}

merged = rock + pop
print(len(merged))                  # 3
print(merged)
# 🎧 Rock + Pop (3 songs, 17:16)
#  1. Bohemian Rhapsody (5:54)
#  2. Stairway to Heaven (8:02)
#  3. Blinding Lights (3:20)