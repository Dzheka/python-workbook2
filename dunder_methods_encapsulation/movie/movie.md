# Movie

Create a Movie class with attributes title, rating (1–10), year.


## Template

```python
m1 = Movie("Inception", 9.2, 2010)
m2 = Movie("Titanic", 8.5, 1997)
m3 = Movie("Inception", 7.0, 2010)

print(m1)          # Inception (2010) — 9.2/10
print(m1 == m3)    # True (same title)
print(m1 > m2)     # True (higher rating)
print(sorted([m2, m1, m3]))
```

<details>
<summary>Hint</summary>

__str__ — "Inception (2010) — 9.2/10"
__eq__ — movies are equal if same title
__gt__, __lt__ — compare by rating

</details>







