class Movie:

    def __init__ (self, title, rating, year):
        self._title = title
        self._rating= rating
        self._year= year
    def __str__(self):
        return f"{self._title}  {(self._year)} -{self._rating}"

m1 = Movie("Inception",9.2, 2010)
m2 = Movie("Titanic", 8.5, 1997)
m3 = Movie("Inception", 7.0, 2010)

print(m1)
