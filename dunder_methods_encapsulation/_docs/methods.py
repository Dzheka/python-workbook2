class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"{self.name} - GPA: {self.gpa}"

    def __eq__(self, other):
        return self.gpa == other.gpa
    
    def __gt__(self, other):
        return self.gpa > other.gpa
    
    def __lt__(self, other):
        return self.gpa < other.gpa

s1 = Student("Ali", 85)
s2 = Student("Sara", 92)
s3 = Student("Nizar", 85)

print(s1 == s3)
print(s2 > s1)
print(sorted([s2, s1, s3]))

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)
    
    def __contains__(self, song):
        return song in self.songs
    
    def __str__(self):
        return f"{self.name}: {len(self)} songs"
    
p = Playlist("My mix")
p.add("Despacito")
p.add("Shape of You")

print(len(p))
print("Despacito" in p)
print("Hello" in p)
print(p)