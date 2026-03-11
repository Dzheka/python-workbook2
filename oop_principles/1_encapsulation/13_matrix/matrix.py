class Matrix:
    def __init__(self, matrix_string):
        self._rows = []
        lines = matrix_string.strip().split("\n")
        for line in lines:
            numbers = line.split()
            row = []
            for num in numbers:
                row.append(int(num))
            self._rows.append(row)

    def row(self, index):
        return self._rows[index-1]
    
    def column(self, index):
        col = []
        for row in self._rows:
            col.append(row[index - 1])
        return col
    
    def get_rows(self):
        return self._rows
    
    def get_columns(self):
        cols = []
        for i in range(len(self._rows[0])):
            col = []
            for row in self._rows:
                col.append(row[i])
            cols.append(col)
        return cols
    
    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self._rows)
    
matrix_string = "9 8 7\n5 3 2\n6 6 7"
matrix = Matrix(matrix_string)

# Access individual rows and columns
print(matrix.row(1))     # [9, 8, 7]
print(matrix.column(2))  # [8, 3, 6]

# Access all rows and columns
print(matrix.get_rows())       # [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
print(matrix.get_columns())    # [[9, 5, 6], [8, 3, 6], [7, 2, 7]]