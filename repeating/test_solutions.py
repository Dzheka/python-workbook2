"""Pytest test suite for all 30 Python tasks.

Run: `pytest test_solutions.py -v`
Optionally: `pytest test_solutions.py -v -k easy` to run only easy tests.
"""

import os
import tempfile
import textwrap

import pytest

import solutions as s


# ============================================================
# EASY
# ============================================================

class TestEasy:
    # E1
    def test_is_even(self):
        assert s.is_even(4) is True
        assert s.is_even(7) is False
        assert s.is_even(0) is True
        assert s.is_even(-2) is True
        assert s.is_even(-3) is False

    # E2
    def test_sum_list(self):
        assert s.sum_list([1, 2, 3]) == 6
        assert s.sum_list([]) == 0
        assert s.sum_list([-5, 5]) == 0
        assert s.sum_list([1.5, 2.5]) == 4.0

    # E3
    def test_count_vowels(self):
        assert s.count_vowels("Hello") == 2
        assert s.count_vowels("PYTHON") == 1
        assert s.count_vowels("xyz") == 0
        assert s.count_vowels("") == 0
        assert s.count_vowels("AEIOUaeiou") == 10

    # E4
    def test_reverse_string(self):
        assert s.reverse_string("hello") == "olleh"
        assert s.reverse_string("") == ""
        assert s.reverse_string("a") == "a"
        assert s.reverse_string("ab") == "ba"

    # E5
    def test_max_of_three(self):
        assert s.max_of_three(1, 2, 3) == 3
        assert s.max_of_three(10, 5, 7) == 10
        assert s.max_of_three(-1, -2, -3) == -1
        assert s.max_of_three(5, 5, 5) == 5

    # E6
    def test_fizzbuzz(self):
        assert s.fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
        assert s.fizzbuzz(15)[-1] == "FizzBuzz"
        assert s.fizzbuzz(15)[2] == "Fizz"
        assert s.fizzbuzz(15)[4] == "Buzz"
        assert s.fizzbuzz(0) == []

    # E7
    def test_count_words(self):
        assert s.count_words("hello world") == 2
        assert s.count_words("   one   two   three  ") == 3
        assert s.count_words("") == 0
        assert s.count_words("    ") == 0
        assert s.count_words("solo") == 1

    # E8
    def test_only_positive(self):
        assert s.only_positive([1, -2, 3, 0, -5, 4]) == [1, 3, 4]
        assert s.only_positive([-1, -2]) == []
        assert s.only_positive([]) == []
        assert s.only_positive([0, 0, 0]) == []

    # E9
    def test_dict_from_keys(self):
        assert s.dict_from_keys(["a", "b", "c"]) == {"a": 0, "b": 0, "c": 0}
        assert s.dict_from_keys(["x", "y"], default=10) == {"x": 10, "y": 10}
        assert s.dict_from_keys([]) == {}

    # E10
    def test_is_palindrome(self):
        assert s.is_palindrome("racecar") is True
        assert s.is_palindrome("A man, a plan, a canal: Panama") is True
        assert s.is_palindrome("hello") is False
        assert s.is_palindrome("") is True
        assert s.is_palindrome("Was it a car or a cat I saw?") is True


# ============================================================
# MEDIUM
# ============================================================

class TestMedium:
    # M1
    def test_group_by_length(self):
        assert s.group_by_length(["a", "bb", "cc", "ddd"]) == {
            1: ["a"], 2: ["bb", "cc"], 3: ["ddd"]
        }
        assert s.group_by_length([]) == {}

    # M2
    def test_flatten(self):
        assert s.flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
        assert s.flatten([[[1]]]) == [1]
        assert s.flatten(["abc", [1, 2]]) == ["abc", 1, 2]
        assert s.flatten([]) == []

    # M3
    def test_word_frequency(self):
        assert s.word_frequency("Hello, hello world!") == {"hello": 2, "world": 1}
        assert s.word_frequency("") == {}
        assert s.word_frequency("A a a") == {"a": 3}

    # M4
    def test_fibonacci_generator(self):
        gen = s.fibonacci_generator(7)
        assert hasattr(gen, "__next__")  # confirm it's a generator
        assert list(s.fibonacci_generator(7)) == [0, 1, 1, 2, 3, 5, 8]
        assert list(s.fibonacci_generator(0)) == []
        assert list(s.fibonacci_generator(-3)) == []
        assert list(s.fibonacci_generator(1)) == [0]
        assert list(s.fibonacci_generator(2)) == [0, 1]

    # M5
    def test_merge_sorted(self):
        assert s.merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
        assert s.merge_sorted([], [1, 2]) == [1, 2]
        assert s.merge_sorted([1, 2], []) == [1, 2]
        assert s.merge_sorted([1, 1], [1, 1]) == [1, 1, 1, 1]
        assert s.merge_sorted([], []) == []

    # M6
    def test_transpose(self):
        assert s.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
        assert s.transpose([[1]]) == [[1]]
        assert s.transpose([]) == []
        assert s.transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]

    # M7
    def test_caesar_cipher(self):
        assert s.caesar_cipher("abc", 1) == "bcd"
        assert s.caesar_cipher("XYZ", 3) == "ABC"
        assert s.caesar_cipher("Hello, World!", 13) == "Uryyb, Jbeyq!"
        assert s.caesar_cipher("abc", -1) == "zab"
        assert s.caesar_cipher("abc", 0) == "abc"
        assert s.caesar_cipher("abc", 26) == "abc"

    # M8
    def test_top_k_frequent(self):
        assert s.top_k_frequent(["a", "b", "a", "c", "b", "a"], 2) == ["a", "b"]
        assert s.top_k_frequent([1, 2, 3], 5) == [1, 2, 3]
        assert s.top_k_frequent([], 3) == []
        assert s.top_k_frequent(["x"], 1) == ["x"]

    # M9
    def test_parse_csv_line(self):
        assert s.parse_csv_line("a,b,c") == ["a", "b", "c"]
        assert s.parse_csv_line('"hello, world",foo,bar') == ["hello, world", "foo", "bar"]
        assert s.parse_csv_line("") == [""]
        assert s.parse_csv_line("a,,c") == ["a", "", "c"]

    # M10
    def test_validate_password(self):
        assert s.validate_password("Abcdef1!") is True
        assert s.validate_password("short1!") is False         # too short
        assert s.validate_password("noDigit!") is False         # no digit
        assert s.validate_password("NoSpecial1") is False       # no special
        assert s.validate_password("nouppercase1!") is False    # no uppercase
        assert s.validate_password("NOLOWERCASE1!") is False    # no lowercase


# ============================================================
# HARD
# ============================================================

class TestHardMemoize:
    def test_basic_caching(self):
        calls = []

        @s.memoize
        def f(x):
            calls.append(x)
            return x * x

        assert f(3) == 9
        assert f(3) == 9
        assert f(4) == 16
        assert calls == [3, 4]

    def test_cache_attribute(self):
        @s.memoize
        def f(x):
            return x

        f(5)
        assert isinstance(f.cache, dict)
        assert len(f.cache) == 1

    def test_cache_clear(self):
        @s.memoize
        def f(x):
            return x

        f(1); f(2); f(3)
        assert len(f.cache) == 3
        f.cache_clear()
        assert len(f.cache) == 0

    def test_kwargs(self):
        @s.memoize
        def f(a, b=1):
            return a + b

        assert f(1, b=2) == 3
        assert f(1, b=2) == 3
        assert len(f.cache) == 1


class TestHardRetry:
    def test_succeeds_first_try(self):
        @s.retry(times=3)
        def good():
            return "ok"

        assert good() == "ok"

    def test_retries_then_succeeds(self):
        attempts = {"n": 0}

        @s.retry(times=3, exceptions=(ValueError,))
        def flaky():
            attempts["n"] += 1
            if attempts["n"] < 2:
                raise ValueError("nope")
            return "done"

        assert flaky() == "done"
        assert attempts["n"] == 2

    def test_all_attempts_fail(self):
        @s.retry(times=2, exceptions=(ValueError,))
        def always_fails():
            raise ValueError("boom")

        with pytest.raises(ValueError, match="boom"):
            always_fails()

    def test_invalid_times(self):
        with pytest.raises(ValueError):
            s.retry(times=0)
        with pytest.raises(ValueError):
            s.retry(times=-1)

    def test_unmatched_exception_propagates(self):
        @s.retry(times=3, exceptions=(ValueError,))
        def raises_type():
            raise TypeError("different")

        with pytest.raises(TypeError):
            raises_type()


class TestHardLRU:
    def test_basic(self):
        c = s.LRUCache(2)
        c.put("a", 1)
        c.put("b", 2)
        assert c.get("a") == 1
        c.put("c", 3)  # evicts b (a was just used)
        assert c.get("b") is None
        assert c.get("a") == 1
        assert c.get("c") == 3

    def test_len(self):
        c = s.LRUCache(3)
        assert len(c) == 0
        c.put("a", 1); c.put("b", 2)
        assert len(c) == 2

    def test_overwrite_does_not_evict(self):
        c = s.LRUCache(2)
        c.put("a", 1); c.put("b", 2)
        c.put("a", 99)  # overwrite, not eviction
        assert len(c) == 2
        assert c.get("a") == 99

    def test_eviction_order(self):
        c = s.LRUCache(2)
        c.put("a", 1); c.put("b", 2)
        c.get("a")           # a is now most recent
        c.put("c", 3)        # should evict b
        assert c.get("b") is None
        assert c.get("a") == 1


class TestHardLogParser:
    def test_valid(self):
        line = "2026-04-15 10:23:01 [INFO] auth: user logged in"
        assert s.parse_log_line(line) == {
            "ts": "2026-04-15 10:23:01",
            "level": "INFO",
            "component": "auth",
            "message": "user logged in",
        }

    def test_error_level(self):
        line = "2026-01-01 00:00:00 [ERROR] db: connection lost"
        result = s.parse_log_line(line)
        assert result["level"] == "ERROR"
        assert result["component"] == "db"

    def test_invalid(self):
        with pytest.raises(ValueError, match="invalid log line"):
            s.parse_log_line("not a log line")
        with pytest.raises(ValueError):
            s.parse_log_line("2026-04-15 10:23:01 [TRACE] x: y")  # bad level


class TestHardEventEmitter:
    def test_subscribe_and_emit(self):
        em = s.EventEmitter()
        log = []
        em.on("greet", lambda name: log.append(f"hi {name}"))
        em.emit("greet", "Alice")
        assert log == ["hi Alice"]

    def test_multiple_handlers(self):
        em = s.EventEmitter()
        log = []
        em.on("ev", lambda: log.append(1))
        em.on("ev", lambda: log.append(2))
        em.emit("ev")
        assert log == [1, 2]

    def test_off(self):
        em = s.EventEmitter()
        log = []
        h = lambda: log.append("x")
        em.on("ev", h)
        em.off("ev", h)
        em.emit("ev")
        assert log == []

    def test_emit_no_subscribers_silent(self):
        em = s.EventEmitter()
        em.emit("nothing")  # must not raise

    def test_off_removes_only_one(self):
        em = s.EventEmitter()
        log = []
        h = lambda: log.append("hit")
        em.on("ev", h); em.on("ev", h)
        em.off("ev", h)
        em.emit("ev")
        assert log == ["hit"]


class TestHardPolynomial:
    def test_call(self):
        p = s.Polynomial([1, 2, 3])
        assert p(2) == 1 + 2 * 2 + 3 * 4  # 17
        assert p(0) == 1

    def test_add_same_length(self):
        p = s.Polynomial([1, 2, 3])
        q = s.Polynomial([10, 20, 30])
        assert (p + q).coeffs == [11, 22, 33]

    def test_add_different_length(self):
        p = s.Polynomial([1, 2, 3])
        q = s.Polynomial([0, 0, 0, 4])
        assert (p + q).coeffs == [1, 2, 3, 4]

    def test_eq_strips_trailing_zeros(self):
        assert s.Polynomial([1, 0]) == s.Polynomial([1])
        assert s.Polynomial([1, 2, 0, 0]) == s.Polynomial([1, 2])

    def test_repr(self):
        assert repr(s.Polynomial([1, 2, 3])) == "Polynomial([1, 2, 3])"
        assert repr(s.Polynomial([1, 0])) == "Polynomial([1])"
        assert repr(s.Polynomial([])) == "Polynomial([0])"
        assert repr(s.Polynomial([0])) == "Polynomial([0])"

    def test_empty_evaluates_to_zero(self):
        assert s.Polynomial([])(5) == 0


class TestHardCsvReader:
    def test_basic(self, tmp_path):
        path = tmp_path / "data.csv"
        path.write_text("name,age\nAlice,30\nBob,25\n", encoding="utf-8")
        rows = list(s.read_csv_dicts(str(path)))
        assert rows == [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]

    def test_quoted_fields(self, tmp_path):
        path = tmp_path / "data.csv"
        path.write_text('a,b\n"hello, world",1\n', encoding="utf-8")
        rows = list(s.read_csv_dicts(str(path)))
        assert rows == [{"a": "hello, world", "b": "1"}]

    def test_skip_blank_lines(self, tmp_path):
        path = tmp_path / "data.csv"
        path.write_text("x,y\n1,2\n\n3,4\n", encoding="utf-8")
        rows = list(s.read_csv_dicts(str(path)))
        assert rows == [{"x": "1", "y": "2"}, {"x": "3", "y": "4"}]

    def test_is_generator(self, tmp_path):
        path = tmp_path / "data.csv"
        path.write_text("x\n1\n", encoding="utf-8")
        gen = s.read_csv_dicts(str(path))
        assert hasattr(gen, "__next__")


class TestHardGroupBy:
    def test_callable_key(self):
        result = s.group_by([1, 2, 3, 4], lambda x: x % 2)
        assert result == {1: [1, 3], 0: [2, 4]}

    def test_string_key_dict(self):
        items = [{"x": 1}, {"x": 2}, {"x": 1}]
        assert s.group_by(items, "x") == {1: [{"x": 1}, {"x": 1}], 2: [{"x": 2}]}

    def test_string_key_attr(self):
        class Obj:
            def __init__(self, val):
                self.val = val

        items = [Obj(1), Obj(2), Obj(1)]
        result = s.group_by(items, "val")
        assert set(result.keys()) == {1, 2}
        assert len(result[1]) == 2

    def test_empty(self):
        assert s.group_by([], lambda x: x) == {}


class TestHardDumps:
    def test_primitives(self):
        assert s.dumps(None) == "null"
        assert s.dumps(True) == "true"
        assert s.dumps(False) == "false"
        assert s.dumps(42) == "42"
        assert s.dumps(3.14) == "3.14"

    def test_strings(self):
        assert s.dumps("hello") == '"hello"'
        assert s.dumps('he said "hi"') == '"he said \\"hi\\""'
        assert s.dumps("line1\nline2") == '"line1\\nline2"'
        assert s.dumps("a\tb") == '"a\\tb"'

    def test_list(self):
        assert s.dumps([1, 2, 3]) == "[1, 2, 3]"
        assert s.dumps([]) == "[]"
        assert s.dumps([1, "a", True]) == '[1, "a", true]'

    def test_dict(self):
        assert s.dumps({"a": 1}) == '{"a": 1}'
        assert s.dumps({}) == "{}"

    def test_nested(self):
        result = s.dumps({"name": "Alice", "scores": [1, 2, 3]})
        assert result == '{"name": "Alice", "scores": [1, 2, 3]}'

    def test_tuple_as_array(self):
        assert s.dumps((1, 2, 3)) == "[1, 2, 3]"

    def test_unsupported(self):
        with pytest.raises(TypeError):
            s.dumps(set([1, 2]))
        with pytest.raises(TypeError):
            s.dumps({1: "non-string key"})


class TestHardFlaskApp:
    def test_post_creates_item(self):
        app = s.create_app()
        client = app.test_client()
        r = client.post("/items", json={"name": "Apple", "price": 1.5})
        assert r.status_code == 201
        body = r.get_json()
        assert body["name"] == "Apple"
        assert body["price"] == 1.5
        assert isinstance(body["id"], int)

    def test_post_invalid_400(self):
        app = s.create_app()
        client = app.test_client()
        r = client.post("/items", json={"name": "Apple"})  # no price
        assert r.status_code == 400
        r = client.post("/items", json={"price": 1.5})  # no name
        assert r.status_code == 400
        r = client.post("/items", json={"name": "Apple", "price": "free"})
        assert r.status_code == 400

    def test_get_list(self):
        app = s.create_app()
        client = app.test_client()
        client.post("/items", json={"name": "A", "price": 1})
        client.post("/items", json={"name": "B", "price": 2})
        r = client.get("/items")
        assert r.status_code == 200
        assert len(r.get_json()) == 2

    def test_get_one(self):
        app = s.create_app()
        client = app.test_client()
        created = client.post("/items", json={"name": "X", "price": 9}).get_json()
        item_id = created["id"]
        r = client.get(f"/items/{item_id}")
        assert r.status_code == 200
        assert r.get_json()["name"] == "X"

    def test_get_missing_404(self):
        app = s.create_app()
        client = app.test_client()
        r = client.get("/items/999")
        assert r.status_code == 404

    def test_delete(self):
        app = s.create_app()
        client = app.test_client()
        created = client.post("/items", json={"name": "X", "price": 9}).get_json()
        item_id = created["id"]
        r = client.delete(f"/items/{item_id}")
        assert r.status_code == 204
        r = client.delete(f"/items/{item_id}")
        assert r.status_code == 404

    def test_initial_items(self):
        app = s.create_app(initial_items=[
            {"name": "Pre1", "price": 10},
            {"name": "Pre2", "price": 20},
        ])
        client = app.test_client()
        r = client.get("/items")
        assert len(r.get_json()) == 2

    def test_independent_state(self):
        app1 = s.create_app()
        app2 = s.create_app()
        c1 = app1.test_client()
        c2 = app2.test_client()
        c1.post("/items", json={"name": "OnlyInApp1", "price": 1})
        r2 = c2.get("/items")
        assert r2.get_json() == []