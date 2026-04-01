class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add(self, title, duration):
        self.songs.append({"title": title, "duration": duration})

    def __len__(self):
        return len(self.songs)

    def __contains__(self, title):
        return any(song["title"] == title for song in self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __add__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented
        new_playlist = Playlist(f"{self.name} + {other.name}")
        new_playlist.songs = self.songs + other.songs
        return new_playlist

    def __eq__(self, other):
        if not isinstance(other, Playlist):
            return False
        return self.songs == other.songs

    def __str__(self):
        total_seconds = sum(song["duration"] for song in self.songs)
        total_minutes = total_seconds // 60
        total_remain = total_seconds % 60

        lines = [
            f"🎧 {self.name} ({len(self)} songs, {total_minutes:02}:{total_remain:02})"
        ]

        for i, song in enumerate(self.songs, start=1):
            minutes = song["duration"] // 60
            seconds = song["duration"] % 60
            lines.append(f" {i}. {song['title']} ({minutes}:{seconds:02})")

        return "\n".join(lines)
