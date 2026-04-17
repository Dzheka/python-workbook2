# PostgreSQL with Flask
## Study Materials & Assignments

---

## Setup with uv

`uv` is a modern Python package manager. It replaces `pip` and manages your virtual environment automatically.

### Install uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Start a new project

```bash
uv init calculator
cd calculator
uv add flask psycopg2-binary python-dotenv matplotlib
```

### Run your app

```bash
uv run python app.py
```

### Comparison with pip

| pip | uv |
|---|---|
| `pip install flask` | `uv add flask` |
| `pip install -r requirements.txt` | `uv sync` |
| `python app.py` | `uv run python app.py` |

uv generates a `pyproject.toml` file that replaces `requirements.txt`.

---

## What is PostgreSQL?

PostgreSQL is an open-source relational database. It stores data in tables with rows and columns, enforces data types, and allows you to query data with SQL.

A plain text file cannot:
- be searched efficiently
- handle multiple users writing at the same time
- enforce that a field is always a number

A database can do all of this.

---

## Core SQL

### Create a table

```sql
CREATE TABLE calculations (
    id         SERIAL PRIMARY KEY,
    expression TEXT NOT NULL,
    result     NUMERIC,
    operation  VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW()
);
```

- `SERIAL` — auto-incrementing integer
- `PRIMARY KEY` — uniquely identifies each row
- `NOT NULL` — this field cannot be empty
- `DEFAULT NOW()` — automatically stores the current timestamp

### Insert

```sql
INSERT INTO calculations (expression, result, operation)
VALUES ('sqrt(144)', 12.0, 'sqrt');
```

### Select

```sql
-- All rows
SELECT * FROM calculations;

-- Specific columns
SELECT expression, result FROM calculations;

-- With filter
SELECT * FROM calculations WHERE operation = 'sqrt';

-- Case-insensitive text search
SELECT * FROM calculations WHERE expression ILIKE '%sin%';

-- Ordered
SELECT * FROM calculations ORDER BY created_at DESC;

-- Limited
SELECT * FROM calculations LIMIT 10;
```

### Update

```sql
UPDATE calculations SET result = 13.0 WHERE id = 1;
```

### Delete

```sql
DELETE FROM calculations WHERE id = 1;
```

### Aggregate functions

```sql
SELECT COUNT(*)     FROM calculations;
SELECT AVG(result)  FROM calculations;
SELECT MAX(result)  FROM calculations;
SELECT MIN(result)  FROM calculations;

-- Count by operation type
SELECT operation, COUNT(*) AS total
FROM calculations
GROUP BY operation
ORDER BY total DESC;
```

---

## Connecting Python to PostgreSQL

```bash
uv add psycopg2-binary
```

### Basic connection

```python
import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    host='localhost',
    database='calculator_db',
    user='postgres',
    password='yourpassword'
)

with conn.cursor(cursor_factory=RealDictCursor) as cur:
    cur.execute("SELECT * FROM calculations")
    rows = cur.fetchall()  # list of dicts

conn.close()
```

`RealDictCursor` returns rows as dictionaries instead of tuples:

```python
# Without RealDictCursor
row[1]              # fragile — depends on column order

# With RealDictCursor
row['expression']   # clear and safe
```

### After INSERT / UPDATE / DELETE — always commit

```python
with conn.cursor() as cur:
    cur.execute("INSERT INTO calculations (expression, result, operation) VALUES (%s, %s, %s)",
                ('10 + 5', 15.0, '+'))
    conn.commit()  # without this, the change is lost
```

### fetchone vs fetchall

```python
cur.fetchone()   # returns one row (dict) or None
cur.fetchall()   # returns list of all rows
```

---

## Credentials — Use Environment Variables

Never hardcode your database password in your Python files.

Create a `.env` file in your project root:

```
DB_HOST=localhost
DB_NAME=calculator_db
DB_USER=postgres
DB_PASSWORD=yourpassword
```

Add `.env` to `.gitignore` so it is never committed.

Load it in Python:

```bash
uv add python-dotenv
```

```python
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host':     os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'calculator_db'),
    'user':     os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', ''),
}
```

---

## SQL Injection — Why %s Matters

Never build SQL queries with f-strings or string concatenation when using user input:

```python
# DANGEROUS — never do this
operation = request.form.get('operation')
cur.execute(f"SELECT * FROM calculations WHERE operation = '{operation}'")
```

If a user enters `' OR '1'='1` the query becomes:

```sql
SELECT * FROM calculations WHERE operation = '' OR '1'='1'
```

This returns every row in the table.

Always use parameterized queries:

```python
# SAFE — always do this
cur.execute("SELECT * FROM calculations WHERE operation = %s", (operation,))
```

The `%s` placeholder tells psycopg2 to sanitize the input before inserting it.

---

## Project Structure

```
calculator/
├── .env
├── pyproject.toml
├── app.py
├── calculator.py
├── database.py
└── templates/
    ├── index.html
    ├── history.html
    └── stats.html
```

---

## database.py — Starter Code

```python
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host':     os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'calculator_db'),
    'user':     os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', ''),
}

class Database:
    def get_connection(self):
        return psycopg2.connect(**DB_CONFIG)

    def save_calculation(self, expression, result, operation):
        # TODO: Assignment 6
        pass

    def get_all(self):
        # TODO: Assignment 6
        pass

    def clear_all(self):
        # TODO: Assignment 6
        pass

    def get_by_operation(self, operation):
        # TODO: Assignment 7
        pass

    def search(self, keyword):
        # TODO: Assignment 7
        pass

    def get_stats(self):
        # TODO: Assignment 8
        pass

    def delete_by_id(self, record_id):
        # TODO: Assignment 9
        pass
```

---

## SQL to Create the Table

Run this in `psql` before starting:

```sql
CREATE DATABASE calculator_db;
\c calculator_db

CREATE TABLE calculations (
    id         SERIAL PRIMARY KEY,
    expression TEXT NOT NULL,
    result     NUMERIC,
    operation  VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

---

## Assignments
### Extending the Flask Calculator with PostgreSQL

> These assignments extend the calculator project from previous lessons.
> Replace `history.txt` with PostgreSQL. All previous features must continue to work.
> All Python code must be written by yourself. AI may be used for HTML and CSS only.

---

### Assignment 6 — Migrate from File to Database

**Difficulty: Medium**

Replace `HistoryManager` with the `Database` class backed by PostgreSQL.

1. Implement `save_calculation(expression, result, operation)` — insert one row
2. Implement `get_all()` — return all rows ordered by `created_at DESC`
3. Implement `clear_all()` — delete all rows
4. Replace all `HistoryManager` calls in `app.py` with `Database`
5. The `/history` page must show: expression, result, operation, timestamp
6. The "Clear History" button must delete all rows from the database

---

### Assignment 7 — Filter and Search

**Difficulty: Medium**

1. Implement `get_by_operation(operation)` — return rows matching the operation
2. Add a dropdown on `/history` to filter by operation
3. Filtering must update the URL: `/history?operation=sqrt`
4. Implement `search(keyword)` using `ILIKE` for case-insensitive search:
   ```sql
   SELECT * FROM calculations WHERE expression ILIKE %s
   -- pass '%keyword%' as the parameter
   ```
5. Add a search input on `/history`
6. Search and filter must work independently and together

---

### Assignment 8 — Statistics from the Database

**Difficulty: Medium**

1. Implement `get_stats()` using SQL aggregate functions — do not load all rows into Python
2. It must return: `total_calculations`, `average_result`, `largest_result`, `smallest_result`, `most_used_operation`
3. Use `GROUP BY` with `ORDER BY COUNT(*) DESC LIMIT 1` for most used operation
4. Update `/stats` to use this method
5. The matplotlib chart on `/stats/chart` must read results from the database

Hint:
```sql
SELECT COUNT(*), AVG(result), MAX(result), MIN(result) FROM calculations;

SELECT operation, COUNT(*) AS cnt
FROM calculations
GROUP BY operation
ORDER BY cnt DESC
LIMIT 1;
```

---

### Assignment 9 — Update the REST API

**Difficulty: Medium-Hard**

1. Update `POST /api/calculate` to save results to PostgreSQL with `[API]` prefix
2. Add `GET /api/history` — returns all calculations as JSON
3. Add `GET /api/stats` — returns stats as JSON using `Database.get_stats()`
4. Add `DELETE /api/history/<int:id>` — deletes one row by ID

Response format for DELETE:
```json
{"success": true}
```

Or on error:
```json
{"success": false, "error": "Record not found."}
```

Implement `delete_by_id(record_id)` in `Database`. Include Postman or curl screenshots in your submission.

---

### Assignment 10 — Multiple Tables and Relations

**Difficulty: Hard**

1. Create a second table:

```sql
CREATE TABLE sessions (
    id         SERIAL PRIMARY KEY,
    session_id VARCHAR(64) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
```

2. Add a foreign key to `calculations`:

```sql
ALTER TABLE calculations ADD COLUMN session_id INTEGER REFERENCES sessions(id);
```

3. Add to `Database`:

```python
def get_or_create_session(self, session_uuid):
    """Insert session if not exists. Return its integer id."""
    pass

def get_by_session(self, session_id):
    """Return all calculations for a given session integer id."""
    pass
```

4. Integrate with Flask sessions from Assignment 3 — each browser session maps to one row in `sessions`
5. `/history` shows only the current session's calculations
6. Add a leaderboard at `/stats` using this query:

```sql
SELECT s.session_id, COUNT(c.id) AS total
FROM sessions s
LEFT JOIN calculations c ON c.session_id = s.id
GROUP BY s.session_id
ORDER BY total DESC;
```

---

## Submission Requirements

For each assignment:

1. All `.py` files including `database.py`
2. A `schema.sql` file with all `CREATE TABLE` statements
3. A `README.md` explaining how to set up and run the project
4. Assignment 9: screenshots of API tests

Submit as `firstname_lastname_assignment_N.zip`

---

## Grading Criteria

| Criterion | Weight |
|---|---|
| Code runs without errors | 25% |
| OOP structure is correct | 25% |
| SQL queries are correct and parameterized | 25% |
| No hardcoded credentials | 15% |
| Code is readable and consistently formatted | 10% |

**Automatic zero** for any SQL query built with f-strings or string concatenation using user input.

Late submissions lose 10% per day.
