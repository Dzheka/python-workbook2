class Movie:
    def __init__(self,title, rating, year):
        self.title = title
        self.rating = rating
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.rating}/10"
    
    def __eq__(self, other):
        return self.title == other.title

    def __gt__(self,other):
        return self.rating > other.rating
    
    def __lt__(self,other):
        return self.rating < other.rating

m1 = Movie("Inception", 9.2, 2010)
m2 = Movie("Titanic", 8.5, 1997)
m3 = Movie("Inception", 7.0, 2010)

print(m1)
print(m1 == m3)
print(m1 > m2)
print(sorted([m2, m1, m3]))