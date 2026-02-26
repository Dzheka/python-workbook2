## `Matrix2x2`

A 2×2 matrix class with `+`, `==`, `print`, and indexing.

- `__init__(self, a, b, c, d)` → stores values as `[[a, b], [c, d]]`
- `__str__` → displays matrix on two lines
- `__eq__` → same values
- `__add__` → element-wise addition, returns new `Matrix2x2`
- `__getitem__(row)` → returns the row as a list (so `m[0][1]` works)

```python
m1 = Matrix2x2(1, 2, 3, 4)
m2 = Matrix2x2(5, 6, 7, 8)

print(m1)
# |1 2|
# |3 4|

print(m1 == Matrix2x2(1, 2, 3, 4))  # True
print(m1[0])       # [1, 2]
print(m1[1][0])    # 3

m3 = m1 + m2
print(m3)
# |6 8|
# |10 12|
```

