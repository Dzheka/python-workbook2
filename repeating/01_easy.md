# Python Tasks - Easy Level

Each task has a strict signature. Implement the function exactly as described so that the automated tests pass.

All solutions go into a single file `solutions.py`. Run `pytest test_solutions.py` to check your work.

---

## Task E1. is_even

Write a function `is_even(n: int) -> bool` that returns `True` if `n` is even and `False` otherwise.

Examples:
- `is_even(4)` returns `True`
- `is_even(7)` returns `False`
- `is_even(0)` returns `True`
- `is_even(-2)` returns `True`

---

## Task E2. sum_list

Write a function `sum_list(numbers: list[float]) -> float` that returns the sum of all numbers in the list. For an empty list it must return `0`.

Examples:
- `sum_list([1, 2, 3])` returns `6`
- `sum_list([])` returns `0`
- `sum_list([-5, 5])` returns `0`

---

## Task E3. count_vowels

Write a function `count_vowels(text: str) -> int` that returns the number of vowels in the string. Vowels are `a, e, i, o, u` in both lower and upper case. Other letters and non-letter characters do not count.

Examples:
- `count_vowels("Hello")` returns `2`
- `count_vowels("PYTHON")` returns `1`
- `count_vowels("xyz")` returns `0`

---

## Task E4. reverse_string

Write a function `reverse_string(text: str) -> str` that returns the string reversed.

Examples:
- `reverse_string("hello")` returns `"olleh"`
- `reverse_string("")` returns `""`
- `reverse_string("a")` returns `"a"`

---

## Task E5. max_of_three

Write a function `max_of_three(a: float, b: float, c: float) -> float` that returns the largest of three numbers. Do not use the built-in `max` function.

Examples:
- `max_of_three(1, 2, 3)` returns `3`
- `max_of_three(10, 5, 7)` returns `10`
- `max_of_three(-1, -2, -3)` returns `-1`

---

## Task E6. fizzbuzz

Write a function `fizzbuzz(n: int) -> list[str]` that returns a list of strings from `1` to `n` inclusive. For multiples of three put `"Fizz"`, for multiples of five `"Buzz"`, for multiples of both `"FizzBuzz"`, otherwise the number itself as a string.

Examples:
- `fizzbuzz(5)` returns `["1", "2", "Fizz", "4", "Buzz"]`
- `fizzbuzz(15)[-1]` returns `"FizzBuzz"`

---

## Task E7. count_words

Write a function `count_words(sentence: str) -> int` that returns the number of words in the sentence. Words are separated by any amount of whitespace. An empty or whitespace-only string returns `0`.

Examples:
- `count_words("hello world")` returns `2`
- `count_words("   one   two   three  ")` returns `3`
- `count_words("")` returns `0`

---

## Task E8. only_positive

Write a function `only_positive(numbers: list[float]) -> list[float]` that returns a new list containing only positive numbers from the input list, in the original order. Zero is not positive.

Examples:
- `only_positive([1, -2, 3, 0, -5, 4])` returns `[1, 3, 4]`
- `only_positive([-1, -2])` returns `[]`

---

## Task E9. dict_from_keys

Write a function `dict_from_keys(keys: list[str], default: int = 0) -> dict[str, int]` that returns a dictionary where each key from `keys` is mapped to `default`.

Examples:
- `dict_from_keys(["a", "b", "c"])` returns `{"a": 0, "b": 0, "c": 0}`
- `dict_from_keys(["x", "y"], default=10)` returns `{"x": 10, "y": 10}`
- `dict_from_keys([])` returns `{}`

---

## Task E10. is_palindrome

Write a function `is_palindrome(text: str) -> bool` that returns `True` if the string reads the same forwards and backwards, ignoring case and non-alphanumeric characters.

Examples:
- `is_palindrome("racecar")` returns `True`
- `is_palindrome("A man, a plan, a canal: Panama")` returns `True`
- `is_palindrome("hello")` returns `False`
- `is_palindrome("")` returns `True`
