class Matrix2x2:
    def __init__(self, a, b, c, d):
        self.data = [[a, b], [c, d]]

    def __str__(self):
        return (
            f"|{self.data[0][0]} {self.data[0][1]}|\n"
            f"|{self.data[1][0]} {self.data[1][1]}|"
        )

    def __eq__(self, other):
        if not isinstance(other, Matrix2x2):
            return False
        return self.data == other.data

    def __add__(self, other):
        if not isinstance(other, Matrix2x2):
            return NotImplemented
        return Matrix2x2(
            self.data[0][0] + other.data[0][0],
            self.data[0][1] + other.data[0][1],
            self.data[1][0] + other.data[1][0],
            self.data[1][1] + other.data[1][1],
        )

    def __getitem__(self, row):
        return self.data[row]
