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
        new_name = f"{self.name} + {other.name}"
        new_playlist = Playlist(new_name)
        new_playlist.songs = self.songs + other.songs

        return new_playlist


    def __eq__(self, other):
        return self.songs == other.songs


    def __str__(self):
        return  format(self.songs)



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