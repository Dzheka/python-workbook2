# Python Tasks - Medium Level

Each task has a strict signature. Implement the function exactly as described so that the automated tests pass.

All solutions go into a single file `solutions.py`. Run `pytest test_solutions.py` to check your work.

---

## Task M1. group_by_length

Write a function `group_by_length(words: list[str]) -> dict[int, list[str]]` that groups words by their length. Keys are word lengths, values are lists of words of that length in the original order.

Examples:
- `group_by_length(["a", "bb", "cc", "ddd"])` returns `{1: ["a"], 2: ["bb", "cc"], 3: ["ddd"]}`
- `group_by_length([])` returns `{}`

---

## Task M2. flatten

Write a function `flatten(nested: list) -> list` that takes a list which may contain other lists nested to any depth and returns a flat list with all elements in their original order. Strings are not unpacked.

Examples:
- `flatten([1, [2, [3, 4]], 5])` returns `[1, 2, 3, 4, 5]`
- `flatten([[[1]]])` returns `[1]`
- `flatten(["abc", [1, 2]])` returns `["abc", 1, 2]`

---

## Task M3. word_frequency

Write a function `word_frequency(text: str) -> dict[str, int]` that returns a dictionary mapping each word to its number of occurrences. Comparison is case-insensitive. Punctuation must be stripped: only the characters `a-z` and `0-9` count as part of a word.

Examples:
- `word_frequency("Hello, hello world!")` returns `{"hello": 2, "world": 1}`
- `word_frequency("")` returns `{}`

---

## Task M4. fibonacci_generator

Write a generator function `fibonacci_generator(n: int)` that yields the first `n` Fibonacci numbers starting with `0, 1, 1, 2, 3, 5, ...`. For `n <= 0` it must yield nothing.

Examples:
- `list(fibonacci_generator(7))` returns `[0, 1, 1, 2, 3, 5, 8]`
- `list(fibonacci_generator(0))` returns `[]`
- `list(fibonacci_generator(1))` returns `[0]`

---

## Task M5. merge_sorted

Write a function `merge_sorted(a: list[int], b: list[int]) -> list[int]` that merges two already-sorted lists into one sorted list, without using `sorted()` or `list.sort()`.

Examples:
- `merge_sorted([1, 3, 5], [2, 4, 6])` returns `[1, 2, 3, 4, 5, 6]`
- `merge_sorted([], [1, 2])` returns `[1, 2]`
- `merge_sorted([1, 1], [1, 1])` returns `[1, 1, 1, 1]`

---

## Task M6. transpose

Write a function `transpose(matrix: list[list]) -> list[list]` that returns the transpose of a rectangular matrix. The input is a list of rows; the output is a list of columns. An empty matrix returns an empty list.

Examples:
- `transpose([[1, 2, 3], [4, 5, 6]])` returns `[[1, 4], [2, 5], [3, 6]]`
- `transpose([[1]])` returns `[[1]]`
- `transpose([])` returns `[]`

---

## Task M7. caesar_cipher

Write a function `caesar_cipher(text: str, shift: int) -> str` that applies a Caesar cipher to each English letter. Shift is applied modulo 26. Letter case is preserved. Non-letter characters are left unchanged.

Examples:
- `caesar_cipher("abc", 1)` returns `"bcd"`
- `caesar_cipher("XYZ", 3)` returns `"ABC"`
- `caesar_cipher("Hello, World!", 13)` returns `"Uryyb, Jbeyq!"`
- `caesar_cipher("abc", -1)` returns `"zab"`

---

## Task M8. top_k_frequent

Write a function `top_k_frequent(items: list, k: int) -> list` that returns the `k` most frequent elements, sorted by frequency descending. Ties are broken by first appearance in the original list.

Examples:
- `top_k_frequent(["a", "b", "a", "c", "b", "a"], 2)` returns `["a", "b"]`
- `top_k_frequent([1, 2, 3], 5)` returns `[1, 2, 3]`
- `top_k_frequent([], 3)` returns `[]`

---

## Task M9. parse_csv_line

Write a function `parse_csv_line(line: str) -> list[str]` that splits a single CSV line into fields. Fields are separated by commas. A field may be wrapped in double quotes, in which case it can contain commas. Surrounding quotes are removed from the result.

Examples:
- `parse_csv_line("a,b,c")` returns `["a", "b", "c"]`
- `parse_csv_line('"hello, world",foo,bar')` returns `["hello, world", "foo", "bar"]`
- `parse_csv_line("")` returns `[""]`

---

## Task M10. validate_password

Write a function `validate_password(password: str) -> bool` that returns `True` only if the password satisfies all rules:
- length is at least 8
- contains at least one lowercase letter
- contains at least one uppercase letter
- contains at least one digit
- contains at least one of `!@#$%^&*`

Examples:
- `validate_password("Abcdef1!")` returns `True`
- `validate_password("short1!")` returns `False`
- `validate_password("noDigit!")` returns `False`
- `validate_password("NoSpecial1")` returns `False`
