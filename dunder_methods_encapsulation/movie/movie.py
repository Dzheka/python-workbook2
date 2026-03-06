class Movie:
    def __init__(self, title, rating,year):
        self.title = title
        self.rating = rating
        self.year = year


    def __str__(self):
        return f"{self.title} {self.year} - {self.year}"

    def __ep__(self,other):
        if self.title == other:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.title == other:
            return True
        else:
            return False

    def __it__(self,other):
        if self.rating > other:
            return True

        else:
            return False



m1 = Movie("Inception", 9.2, 2010)
m2 = Movie("Titanic", 8.5, 1997)
m3 = Movie("Inception", 7.0, 2010)

print(m1)          # Inception (2010) — 9.2/10
print(m1 == m3)    # True (same title)
print(m1 > m2)     # True (higher rating)
print(sorted([m2, m1, m3]))