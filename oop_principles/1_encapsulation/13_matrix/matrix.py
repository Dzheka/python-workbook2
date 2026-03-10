class Matrix:
    def __init__(self, matrix_string):
        self._rows = []
        for line in matrix_string.strip().split("\n"):
            self._rows.append([int(n) for n in line.split()])

    def row(self, index):
        return self._rows[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self._rows]

    def get_rows(self):
        return self._rows

    def get_columns(self):
        num_cols = len(self._rows[0])
        return [self.column(i + 1) for i in range(num_cols)]
