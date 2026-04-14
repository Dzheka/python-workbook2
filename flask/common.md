# 🐍 Flask & uv — Quick Reference for Students

> **📢 Notice:** You still have a chance to finish your last coding task **right now, during today's class.**
> This is your opportunity — ask questions, test your code, and submit before the session ends. Don't leave it for later. You've got this! 💪

---

## Table of Contents

1. [What is HTTP?](#1-what-is-http)
2. [HTTP Methods](#2-http-methods)
3. [HTTP Status Codes](#3-http-status-codes)
4. [What is JSON?](#4-what-is-json)
5. [How Flask Works](#5-how-flask-works)
6. [Core Building Blocks](#6-core-building-blocks)
7. [In-Memory Storage Pattern](#7-in-memory-storage-pattern)
8. [uv — Essential Commands](#8-uv--essential-commands)
9. [Checklist Before You Submit](#9-checklist-before-you-submit)

---

## 1. What is HTTP?

**HTTP** stands for **HyperText Transfer Protocol**.
It is the language that browsers and apps use to talk to servers.

Every interaction has two sides:

```
CLIENT  ──── request  ────▶  SERVER
CLIENT  ◀─── response ────   SERVER
```

Think of it like ordering food at a restaurant:

| Step | Food analogy | HTTP |
|------|-------------|------|
| You place an order | "I'd like a burger" | **Request** |
| Waiter takes it to the kitchen | Routing | **URL + Method** |
| Kitchen prepares the food | Business logic | **View function** |
| Waiter brings the food back | Delivery | **Response** |

---

## 2. HTTP Methods

HTTP methods tell the server **what action** the client wants to perform.

| Method | Purpose | Real example |
|--------|---------|-------------|
| `GET` | Read / retrieve data | Load a list of products |
| `POST` | Create new data | Register a new user |
| `PUT` | Replace existing data entirely | Overwrite a full user profile |
| `PATCH` | Partially update data | Change only the user's email |
| `DELETE` | Remove data | Delete a post |

### Rules to remember

- **GET** — never has a body. Data goes in the **URL** as query params: `/search?q=flask`
- **POST / PUT / PATCH** — carry data in the **request body**, usually as JSON
- **DELETE** — usually no body; the id goes in the **URL**: `/users/5`

---

## 3. HTTP Status Codes

Every response has a **3-digit status code** that tells the client what happened.

### ✅ Success (2xx)

| Code | Name | When to use |
|------|------|-------------|
| `200` | OK | Request succeeded, data returned |
| `201` | Created | A new resource was successfully created |
| `204` | No Content | Success, but nothing to return |

### ⚠️ Client Errors (4xx) — the client did something wrong

| Code | Name | When to use |
|------|------|-------------|
| `400` | Bad Request | Missing or invalid data in the request |
| `401` | Unauthorized | Login required |
| `403` | Forbidden | Logged in but not allowed |
| `404` | Not Found | Resource does not exist |
| `405` | Method Not Allowed | Wrong HTTP method for this route |
| `409` | Conflict | e.g. username already taken |
| `413` | Payload Too Large | Uploaded data exceeds the size limit |

### 🔥 Server Errors (5xx) — something broke on the server

| Code | Name | When to use |
|------|------|-------------|
| `500` | Internal Server Error | Unhandled exception / crash |

---

## 4. What is JSON?

**JSON** stands for **JavaScript Object Notation**.
It is the universal format for sending data in APIs — it looks almost identical to a Python dict.

```json
{
  "id": 1,
  "name": "Ali",
  "age": 20,
  "active": true,
  "scores": [95, 88, 76],
  "address": {
    "city": "Khujand"
  }
}
```

### JSON ↔ Python mapping

| JSON type | Python type | Example |
|-----------|------------|---------|
| `string` | `str` | `"hello"` |
| `number` | `int` / `float` | `42`, `3.14` |
| `boolean` | `bool` | `true` → `True` |
| `null` | `None` | `null` → `None` |
| `array` | `list` | `[1, 2, 3]` |
| `object` | `dict` | `{"key": "val"}` |

> **In Flask:**
> - Receive JSON → `request.json`
> - Send JSON → `jsonify(your_dict)`

---

## 5. How Flask Works

Flask is a **web framework** for Python. It connects URLs to Python functions.

```
Browser            Flask App
  │                   │
  │  GET /hello  ───▶ │  @app.route("/hello")
  │                   │  def hello():
  │                   │      return "Hello!"
  │  "Hello!"   ◀─── │
```

### Minimal working app

```python
from flask import Flask

app = Flask(__name__)           # create the app

@app.route("/hello")            # register the route
def hello():                    # view function
    return "Hello, World!"      # response body

if __name__ == "__main__":
    app.run(debug=True)         # start the server on port 5000
```

Open `http://localhost:5000/hello` → you see `Hello, World!`

---

## 6. Core Building Blocks

### 6.1 Routes and Methods

```python
# GET only (default)
@app.route("/users")
def get_users():
    ...

# POST only
@app.route("/users", methods=["POST"])
def create_user():
    ...

# Both GET and POST on the same URL
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # handle form submission
        ...
    # show the form
    ...
```

---

### 6.2 Dynamic URL Segments

```python
# String (default) — captures anything
@app.route("/users/<username>")
def profile(username):
    return f"Profile: {username}"
# GET /users/ali  →  "Profile: ali"

# Integer — auto-converts to int
@app.route("/users/<int:uid>")
def get_user(uid):
    return f"User id: {uid}"
# GET /users/5  →  "User id: 5"

# Float
@app.route("/price/<float:amount>")
def price(amount):
    ...
```

---

### 6.3 Reading Query Parameters

Query parameters come after `?` in the URL.

```
/search?q=flask&page=2
```

```python
from flask import request

@app.route("/search")
def search():
    q    = request.args.get("q", "")           # default "" if missing
    page = request.args.get("page", 1, type=int)  # auto-convert to int
    return f"Searching '{q}', page {page}"
```

---

### 6.4 Reading POST Form Data

```python
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]          # raises KeyError if missing
    username = request.form.get("username", "")  # safe version with default
    ...
```

---

### 6.5 Reading JSON Body

```python
@app.route("/users", methods=["POST"])
def create():
    data = request.json              # parses body automatically
    name = data["name"]              # access fields like a dict
    age  = data.get("age", 0)        # safe access with default
    ...
```

> **Tip:** The client must send the header `Content-Type: application/json`

---

### 6.6 Sending JSON Responses

```python
from flask import jsonify

# Simple dict
return jsonify({"id": 1, "name": "Ali"})

# With custom status code (default is 200)
return jsonify({"id": 1, "name": "Ali"}), 201

# List
return jsonify([{"id": 1}, {"id": 2}])

# Error response
return jsonify({"error": "not found"}), 404
```

---

### 6.7 Custom Error Handlers

```python
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "resource not found"}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "bad request"}), 400

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "internal server error"}), 500
```

---

### 6.8 Redirect

```python
from flask import redirect, url_for

@app.route("/old-page")
def old():
    return redirect(url_for("new_page"))   # redirect by function name

@app.route("/new-page")
def new_page():
    return "This is the new page"
```

---

### 6.9 Blueprints — Splitting the App into Modules

A **Blueprint** is a mini-app that groups related routes.
You register it on the main app with a URL prefix.

```python
# auth.py
from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return "Login page"

@auth.route("/logout")
def logout():
    return "Logged out"
```

```python
# app.py
from flask import Flask
from auth import auth

app = Flask(__name__)
app.register_blueprint(auth, url_prefix="/auth")

# Routes become:
#   GET /auth/login
#   GET /auth/logout
```

---

## 7. In-Memory Storage Pattern

Since there is no database in this task, store data in **module-level** Python variables.

### List storage

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

items = []    # ← module level, lives for the whole session
next_id = 1   # ← auto-incrementing counter

@app.route("/items", methods=["POST"])
def create_item():
    global next_id                          # ← required when modifying

    data = request.json
    item = {
        "id":   next_id,
        "name": data["name"],
        "done": False
    }
    items.append(item)
    next_id += 1
    return jsonify(item), 201


@app.route("/items")
def get_items():
    return jsonify(items)
```

### Find by id — the standard pattern

```python
@app.route("/items/<int:item_id>")
def get_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)

    if item is None:
        return jsonify({"error": "not found"}), 404

    return jsonify(item)
```

### Update one field

```python
@app.route("/items/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "not found"}), 404

    data = request.json
    for key in ["name", "done"]:        # only update allowed fields
        if key in data:
            item[key] = data[key]

    return jsonify(item)
```

### Delete

```python
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    item = next((i for i in items if i["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "not found"}), 404

    items = [i for i in items if i["id"] != item_id]
    return jsonify({"deleted": item_id})
```

---

## 8. uv — Essential Commands

```bash
# Project setup
uv init myproject          # create a new project folder
cd myproject
uv add flask               # add flask as a dependency
uv add requests            # add any other package
uv add --dev pytest        # add pytest for testing (dev only)

# Running
uv run app.py              # run your script (no manual venv activation needed)

# Syncing
uv sync                    # install everything from uv.lock
uv sync --frozen           # install without changing uv.lock (use in CI/CD)

# Inspecting
uv pip list                # show all installed packages
uv tree                    # show dependency tree

# Removing
uv remove flask            # remove a package
```

### What is `uv.lock`?

`uv.lock` is a **lock file** — it records the exact version of every package
(including indirect dependencies). Commit it to git so every teammate
gets the identical environment when they run `uv sync`.

```
uv add flask   →   updates pyproject.toml  +  uv.lock  →  installs
uv sync        →   reads uv.lock  →  installs exact versions
```

### Why `--dev`?

```bash
uv add --dev pytest
```

Dev dependencies are only needed **while developing** (testing, linting).
They are NOT installed in production, keeping the deployed app lightweight.

---

## 9. Checklist Before You Submit

Go through this list before sending your work:

- [ ] Every route returns **JSON** — use `jsonify()`, never `str(dict)`
- [ ] POST routes have `methods=["POST"]` in `@app.route()`
- [ ] Resources that don't exist return **404** with a JSON error body
- [ ] Invalid or missing input returns **400**
- [ ] Successfully created resources return **201**, not 200
- [ ] The in-memory list / dict is defined at **module level** (outside functions)
- [ ] `global next_id` is declared inside functions that modify the counter
- [ ] Blueprints are registered on the app with `app.register_blueprint(...)`
- [ ] The app starts with `app.run(debug=True)` inside `if __name__ == "__main__":`
- [ ] You tested every route manually (browser, curl, or test client)

---

## 🔥 Common Mistakes

| Mistake | Fix |
|---------|-----|
| `return str(data)` | Use `return jsonify(data)` |
| Returning `200` after creating | Use `return jsonify(data), 201` |
| `items = []` inside a function | Move it to module level |
| Forgetting `global next_id` | Add `global next_id` at the top of the function |
| Route only accepts GET but you POST | Add `methods=["POST"]` |
| `request.json` is `None` | Client must send `Content-Type: application/json` |
| Blueprint routes not found | Check the `url_prefix` on `register_blueprint` |
| No 404 for missing resources | Always check if item exists before returning it |

---

> Good luck — the session is still running, your code editor is open, and the answer is one `uv run app.py` away. 🚀