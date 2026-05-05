# Python Tasks - Hard Level

Each task has a strict signature. Implement the function (or class) exactly as described so that the automated tests pass.

All solutions go into a single file `solutions.py`. Run `pytest test_solutions.py` to check your work.

---

## Task H1. memoize

Write a decorator `memoize(func)` that caches the results of the wrapped function. The cache key is built from positional and keyword arguments. The decorated function must also expose an attribute `cache` (a dict) and a method `cache_clear()`.

Example usage:
```python
@memoize
def slow_square(x):
    return x * x

slow_square(4)              # 16
slow_square.cache            # contains the cached result
slow_square.cache_clear()    # clears it
```

The cache must work for hashable positional and keyword arguments.

---

## Task H2. retry

Write a decorator factory `retry(times: int, exceptions: tuple = (Exception,))`. The wrapped function is called up to `times` times if any of the listed exception types is raised; on the last failure the exception is propagated.

Example:
```python
@retry(times=3, exceptions=(ValueError,))
def flaky(): ...
```

If the function succeeds on attempt `k <= times`, return its result. If all attempts fail, re-raise the last exception. `times` must be a positive integer; otherwise raise `ValueError`.

---

## Task H3. LRUCache class

Implement a class `LRUCache` with the following interface:
- `LRUCache(capacity: int)` creates a cache with the given positive capacity
- `cache.get(key)` returns the value or `None` if missing; counts as a usage
- `cache.put(key, value)` stores a value; if capacity is exceeded, evict the least recently used item
- `len(cache)` returns the current number of items

Both `get` and `put` must run in `O(1)` average time. Use either `collections.OrderedDict` or a manual doubly linked list + dict.

Example:
```python
c = LRUCache(2)
c.put("a", 1); c.put("b", 2)
c.get("a")        # 1
c.put("c", 3)     # evicts "b"
c.get("b")        # None
```

---

## Task H4. parse_log_line

Write a function `parse_log_line(line: str) -> dict` for log lines of the form:
```
2026-04-15 10:23:01 [LEVEL] component: message text
```
The function returns a dict with keys `ts`, `level`, `component`, `message`. If the line does not match this format, raise a `ValueError` with the message `"invalid log line"`.

Allowed levels: `DEBUG, INFO, WARN, ERROR`.

---

## Task H5. EventEmitter class

Implement a class `EventEmitter` with the following interface:
- `emitter.on(event: str, handler)` subscribes a handler to an event
- `emitter.off(event: str, handler)` removes one subscription
- `emitter.emit(event: str, *args, **kwargs)` calls every handler subscribed to the event in subscription order, passing along any arguments
- the same handler may be subscribed multiple times to the same event; `off` removes only one subscription per call
- `emit` on an event with no subscribers does nothing and does not raise

---

## Task H6. Polynomial class

Implement a class `Polynomial` representing a polynomial with integer coefficients given as a list `[a0, a1, a2, ...]` meaning `a0 + a1*x + a2*x^2 + ...`. It must support:
- `Polynomial([1, 2, 3])` constructor
- `p(x)` evaluation at `x` (`__call__`)
- `p1 + p2` returns a new `Polynomial` (different lengths handled correctly)
- `p1 == p2` compares coefficients (trailing zeros are equivalent: `Polynomial([1, 0])` equals `Polynomial([1])`)
- `repr(p)` returns `"Polynomial([1, 2, 3])"` with **trailing zeros stripped** (so `Polynomial([1, 0])` repr is `"Polynomial([1])"`)
- the empty polynomial `Polynomial([])` and `Polynomial([0])` both repr as `"Polynomial([0])"` and evaluate to `0`

---

## Task H7. read_csv_dicts (generator)

Write a generator function `read_csv_dicts(path: str)` that yields each row of a CSV file as a dict. The first row is treated as the header. The function must:
- be a generator (use `yield`)
- close the file when iteration ends or is interrupted (use a `with` block)
- skip empty lines
- handle quoted fields with internal commas (use the standard `csv` module)

---

## Task H8. group_by

Write a function `group_by(items: list, key) -> dict`:
- `key` may be a callable (applied to each item) or a string (treated as a key/attribute name; first try `item[key]`, then `getattr(item, key)`)
- result is a dict mapping each key value to a list of matching items, in the original order

Examples:
- `group_by([1, 2, 3, 4], lambda x: x % 2)` returns `{1: [1, 3], 0: [2, 4]}`
- `group_by([{"x": 1}, {"x": 2}, {"x": 1}], "x")` returns `{1: [{"x": 1}, {"x": 1}], 2: [{"x": 2}]}`

---

## Task H9. JSON-style serializer

Write a function `dumps(value) -> str` that serializes a Python value into a JSON-like string by hand (do not use `json.dumps`). Supported types:
- `None` -> `"null"`
- `True` / `False` -> `"true"` / `"false"`
- `int` and `float` -> their `str` representation
- `str` -> a quoted string with `"`, `\`, newline, tab, and carriage return escaped (`\"`, `\\`, `\n`, `\t`, `\r`)
- `list` and `tuple` -> `[elem1, elem2, ...]` with elements serialized recursively
- `dict` (string keys only) -> `{"key": value, ...}` with values serialized recursively

For an unsupported type raise `TypeError`. There must be no trailing comma; use a single space after `:` and `,`.

---

## Task H10. Flask blueprint factory

Write a function `create_app(initial_items: list[dict] | None = None) -> Flask` that returns a fully configured Flask app with an in-memory store. If `initial_items` is given, each item must have keys `name` and `price` (both required). The app exposes:

- `POST /items` -- JSON body `{"name": str, "price": float}`. Returns the created item with auto-generated integer `id`, status `201`. Returns `400` if either field is missing or has a wrong type.
- `GET /items` -- list of all items as JSON.
- `GET /items/<int:item_id>` -- one item or `404`.
- `DELETE /items/<int:item_id>` -- `204` on success, `404` if missing.

Each call to `create_app` must produce an independent store (no shared state between two apps).
