from functools import wraps
from collections import OrderedDict
import re
from flask import Flask, request, jsonify

print("====Task M1: group_by_length====")
def group_by_length(words: list[str]) -> dict[int, list[str]]:
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    return result

print(group_by_length(["a", "bb", "cc", "ddd"]))


print("\n=====Task M2: flatten=====")
def flatten(nested: list) -> list:
    result = []
    for i in nested:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print(flatten([1, [2, [3, 4]], 5]))
print(flatten([[[1]]]))
print(flatten(["abc", [1, 2]]))


print("\n====Task M3: word_frequency====")
def word_frequency(text: str) -> dict[str, int]:
    result = {}
    text = text.lower()
    new = ""
    for i in text:
        if i.isalnum():
            new += i
        else:
            new += " "
    words = new.split()
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result
print(word_frequency("Hello, hello world!"))
print(word_frequency(""))


print("\n===Task M4: fibonacci_generator===")
def fibonacci_generator(n: int):
    if n <= 0:
        return []
    result = []
    a = 0
    b = 1
    for i in range(n):
        result.append(a)
        next = a + b
        a = b
        b = next
    return result
print(list(fibonacci_generator(7)))
print(list(fibonacci_generator(0)))
print(list(fibonacci_generator(1)))


print("\n=====Task M5: merge_sorted=====")
def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result
print(merge_sorted([1, 3, 5], [2, 4, 6]))
print(merge_sorted([], [1, 2]))
print(merge_sorted([1, 1], [1, 1]))


print("\n=====Task M6: transpose=====")
def transpose(matrix: list[list]) -> list[list]:
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
    return result
print(transpose([[1, 2, 3], [4, 5, 6]]))
print(transpose([[1]]))
print(transpose([]))


print("\n=====Task M7: caesar_cipher=====")
def caesar_cipher(text: str, shift: int) -> str:
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift %= 26
    result = ""
    for ch in text:
        if ch in lower:
            idx = lower.index(ch)
            new_idx = (idx + shift) % 26
            result += lower[new_idx]
        elif ch in upper:
            idx = upper.index(ch)
            new_idx = (idx + shift) % 26
            result += upper[new_idx]
        else:
            result += ch
    return result
print(caesar_cipher("abc", 1))
print(caesar_cipher("XYZ", 3))
print(caesar_cipher("Hello, World!", 13))
print(caesar_cipher("abc", -1))


print("\n=====Task M8: top_k_frequent=====")
def top_k_frequent(items: list, k: int) -> list:
    if not items:
        return []
    freq = {}
    order = {}
    for idx, item in enumerate(items):
        freq[item] = freq.get(item, 0) + 1
        if item not in order:
            order[item] = idx
    tuples = []
    for item in freq:
        tuples.append((-freq[item], order[item], item))
    tuples.sort()
    result = [t[2] for t in tuples]
    return result[:k]
print(top_k_frequent(["a", "b", "a", "c", "b", "a"], 2))
print(top_k_frequent([1, 2, 3], 5))
print(top_k_frequent([], 3))


print("\n=====Task M9: parse_csv_line=====")
def parse_csv_line(line: str) -> list[str]:
    result = []
    field = ""
    in_quotes = False
    for ch in line:
        if ch == '"':
            in_quotes = not in_quotes
        elif ch == "," and not in_quotes:
            result.append(field)
            field = ""
        else:
            field += ch
    result.append(field)
    return result
print(parse_csv_line("a,b,c"))
print(parse_csv_line('"hello, world",foo,bar'))
print(parse_csv_line(""))


print("\n=====Task M10: validate_password=====")
def validate_password(password: str) -> bool:
    if len(password) < 0:
        return False
    has_lower = any(ch.islower() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    specials = "!@#$%^&*"
    has_special = any(ch in specials for ch in password)
    return has_lower and has_upper and has_digit and has_special
print(validate_password("Abcdef1!"))
print(validate_password("short1!"))
print(validate_password("noDigit!"))
print(validate_password("NoSpecial1"))




print("\n=====Task H1: memoize=====")
def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    wrapper.cache = cache

    def cache_clear():
        cache.clear()
    wrapper.cache_clear = cache_clear

    return wrapper

@memoize
def slow_square(x, power=2):
    return x ** power
print(slow_square(4))
print(slow_square(4))
print(slow_square.cache)
slow_square.cache_clear()
print(slow_square.cache)


print("\n=====Task H2: retry=====")
def retry(times: int, exceptions: tuple = (Exception,)):
    if times <= 0:
        raise ValueError("times must be a positive integer")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exc = e
                    if attempt == times:
                        raise
            raise last_exc
        return wrapper
    return decorator

@retry(times=3, exceptions=(ValueError,))
def flaky():
    import random
    x = random.randint(0, 1)
    if x == 0:
        raise ValueError("Random fail")
    return "Success!"
print(flaky())


print("\n=====Task H3: LRUCache class=====")
class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def __len__(self):
        return len(self.cache)

c = LRUCache(2)
c.put("a", 1)
c.put("b", 2)
print(c.get("a"))
c.put("c", 3)
print(c.get("b"))
print(len(c))


print("\n=====Task H4: parse_log_line=====")
def parse_log_line(line: str) -> dict:
    pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(DEBUG|INFO|WARN|ERROR)\] ([^:]+): (.+)$"

    match = re.match(pattern, line)
    if not match:
        raise ValueError("invalid log line")

    ts, level, component, message = match.groups()
    return {"ts": ts, "level": level, "component": component, "message": message}


print(parse_log_line("2026-04-15 10:23:01 [INFO] auth: login successful"))
try:
    print(parse_log_line("invalid log line"))
except ValueError as e:
    print(f"Caught expected error: {e}")



print("\n=====Task H5: EventEmitter class=====")
class EventEmitter:
    def __init__(self):
        self._events = {}

    def on(self, event: str, handler):
        self._events.setdefault(event, []).append(handler)

    def off(self, event: str, handler):
        if event in self._events:
            handlers = self._events[event]
            try:
                handlers.remove(handler)
                if not handlers:
                    del self._events[event]
            except ValueError:
                pass

    def emit(self, event: str, *args, **kwargs):
        if event in self._events:
            for handler in list(self._events[event]):
                handler(*args, **kwargs)
def hello(name):
    print("Hello,", name)

def goodbye(name):
    print("Goodbye,", name)

emitter = EventEmitter()
emitter.on("greet", hello)
emitter.on("greet", goodbye)

emitter.emit("greet", "Nizar")

emitter.off("greet", hello)
emitter.emit("greet", "Nizar")


print("\n=====Task H6: Polynomial class=====")
class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = list(map(int, coeffs))
        self._strip_trailing_zeros()

    def _strip_trailing_zeros(self):
        while len(self.coeffs) > 1 and self.coeffs[-1] == 0:
            self.coeffs.pop()
        if not self.coeffs:
            self.coeffs = [0]

    def __call__(self, x):
        result = 0
        for power, coef in enumerate(self.coeffs):
            result += coef * (x**power)
        return result

    def __add__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))
        new_coeffs = []
        for i in range(max_len):
            a = self.coeffs[i] if i < len(self.coeffs) else 0
            b = other.coeffs[i] if i < len(other.coeffs) else 0
            new_coeffs.append(a + b)
        return Polynomial(new_coeffs)

    def __eq__(self, other):
        return self.coeffs == other.coeffs

    def __repr__(self):
        return f"Polynomial({self.coeffs})"
p1 = Polynomial([1, 2, 3])
print(p1(2))

p2 = Polynomial([5, 0, 1])
print(p1 + p2)

print(Polynomial([1, 0]) == Polynomial([1]))
print(repr(Polynomial([0, 0])))
print(repr(Polynomial([])))


print("\n=====Task H7: read_csv_dicts(generator)=====")
import csv
def read_csv_dicts(path: str):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not any(row.values()):
                continue
            yield row
for row in read_csv_dicts("data.csv"):
    print(row)


print("\n=====Task H8: group_by=====")
def group_by(items: list, key) -> dict:
    result = {}
    for item in items:
        if callable(key):
            k = key(item)
        else:
            try:
                k = item[key]  # coba akses dict
            except (TypeError, KeyError):
                k = getattr(item, key)

        result.setdefault(k, []).append(item)
    return result
print(group_by([1, 2, 3, 4], lambda x: x % 2))

print(group_by([{"x": 1}, {"x": 2}, {"x": 1}], "x"))

class Obj:
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return f"Obj({self.val})"

objs = [Obj(1), Obj(2), Obj(1)]
print(group_by(objs, "val"))



print("\n=====Task H9: JSON-style serializer=====")
def dumps(value) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        escaped = (
            value.replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("\n", "\\n")
            .replace("\t", "\\t")
            .replace("\r", "\\r")
        )
        return f'"{escaped}"'
    if isinstance(value, (list, tuple)):
        return "[" + ", ".join(dumps(v) for v in value) + "]"
    if isinstance(value, dict):
        parts = []
        for k, v in value.items():
            if not isinstance(k, str):
                raise TypeError("dict keys must be strings")
            parts.append(dumps(k) + ": " + dumps(v))
        return "{" + ", ".join(parts) + "}"
    raise TypeError(f"Unsupported type: {type(value).__name__}")
print(dumps(None))
print(dumps(True))
print(dumps("Hello\nWorld"))
print(dumps([1, 2, "x"]))
print(dumps({"a": 1, "b": [True, None]}))


print("\n=====Task H10: Flask blueprint factory=====")
def create_app(initial_items: list[dict] | None = None):
    app = Flask(__name__)

    items = {}
    counter = 1

    if initial_items:
        for item in initial_items:
            if not isinstance(item, dict) or "name" not in item or "price" not in item:
                raise ValueError("initial_items must be list of dicts with name and price")
            if not isinstance(item["name"], str) or not isinstance(item["price"], (int, float)):
                raise ValueError("invalid item format")
            nonlocal_counter = counter
            items[nonlocal_counter] = {"id": nonlocal_counter, "name": item["name"], "price": float(item["price"])}
            counter += 1

    @app.post("/items")
    def create_item():
        nonlocal counter
        data = request.get_json()
        if not data or "name" not in data or "price" not in data:
            return jsonify({"error": "Invalid"}), 400
        if not isinstance(data["name"], str) or not isinstance(data["price"], (int, float)):
            return jsonify({"error": "Invalid"}), 400
        item = {"id": counter, "name": data["name"], "price": float(data["price"])}
        items[counter] = item
        counter += 1
        return jsonify(item), 201

    @app.get("/items")
    def list_items():
        return jsonify(list(items.values()))

    @app.get("/items/<int:item_id>")
    def get_item(item_id):
        if item_id not in items:
            return jsonify({"error": "Not found"}), 404
        return jsonify(items[item_id])

    @app.delete("/items/<int:item_id>")
    def delete_item(item_id):
        if item_id not in items:
            return jsonify({"error": "Not found"}), 404
        del items[item_id]
        return "", 204

    return app
if __name__ == "__main__":
    app = create_app([{"name": "apple", "price": 1.2}, {"name": "banana", "price": 0.8}])
    app.run(debug=True)
