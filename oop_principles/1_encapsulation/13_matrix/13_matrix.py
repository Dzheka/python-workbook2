class Matrix:


    def __init__(self, matrix_string):
        self._data = []

        for line in matrix_string.strip().split("\n"):
            row = []
            for num in line.split():
                row.append(int(num))
            self._data.append(row)


    def row(self, index):
        return self._data[index - 1]


    def column(self, index):
        result = []
        for row in self._data:
            result.append(row[index - 1])
        return result


    def get_rows(self):
        return self._data


    def get_columns(self):
        columns = []
        num_cols = len(self._data[0])
        for i in range(1, num_cols + 1):
            columns.append(self.column(i))
        return columns



matrix_string = "9 8 7\n5 3 2\n6 6 7"
matrix = Matrix(matrix_string)

print(matrix.row(1))        # [9, 8, 7]
print(matrix.row(2))        # [5, 3, 2]
print(matrix.column(1))     # [9, 5, 6]
print(matrix.column(2))     # [8, 3, 6]
print(matrix.get_rows())    # [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
print(matrix.get_columns()) # [[9, 5, 6], [8, 3, 6], [7, 2, 7]]
