# Hello World Telegram Bot
### Python · uv · Flask · PostgreSQL — Step-by-Step Guide for Students

---

## What You Will Build

A Telegram bot that:
- Replies "Hello, World!" to any `/start` or `/hello` command
- Logs every message to a PostgreSQL database
- Runs as a Flask web server using webhooks
- Is managed with uv — the modern Python package manager

---

## Final Project Structure

```
telegram-bot/
├── .env
├── .python-version
├── pyproject.toml
├── app.py
└── db.py
```

---

## Prerequisites

| Tool | Purpose | Install |
|------|---------|---------|
| Python 3.11+ | Language | https://python.org |
| uv | Package manager | See Step 1 |
| PostgreSQL | Database | https://postgresql.org |
| ngrok | Expose localhost | https://ngrok.com |
| Telegram account | Create a bot | https://t.me/BotFather |

---

## Step 0 — Create Your Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Send the command `/newbot`
3. Choose a name: e.g. `My Hello Bot`
4. Choose a username (must end in `bot`): e.g. `my_hello_world_bot`
5. BotFather will give you a token that looks like:

```
123456789:AAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> **Important:** Keep this token secret. Never commit it to Git.

---

## Step 1 — Install uv

`uv` is a fast Python package and project manager written in Rust. It replaces `pip`, `venv`, and `pip-tools` in one tool.

**Linux / macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify the installation:
```bash
uv --version
# uv 0.5.x ...
```

---

## Step 2 — Create the Project

```bash
# Create a new project folder and enter it
uv init telegram-bot
cd telegram-bot
```

This creates:
- `pyproject.toml` — project metadata and dependencies
- `.python-version` — pins the Python version
- `hello.py` — starter file (we will replace it)

Pin the Python version:
```bash
uv python pin 3.11
```

---

## Step 3 — Add Dependencies

```bash
uv add flask python-telegram-bot psycopg2-binary python-dotenv
```

What each package does:

| Package | Purpose |
|---------|---------|
| `flask` | Web server to receive webhook updates from Telegram |
| `python-telegram-bot` | Official Telegram Bot API wrapper |
| `psycopg2-binary` | PostgreSQL database driver |
| `python-dotenv` | Load secrets from `.env` file |

After running the command, `pyproject.toml` will be updated automatically.

---

## Step 4 — Set Up PostgreSQL

### 4.1 — Create a database and user

Open the PostgreSQL shell:
```bash
psql -U postgres
```

Run these SQL commands:
```sql
-- Create a dedicated database
CREATE DATABASE telegram_bot_db;

-- Create a user with a password
CREATE USER bot_user WITH PASSWORD 'yourpassword';

-- Grant all privileges
GRANT ALL PRIVILEGES ON DATABASE telegram_bot_db TO bot_user;

-- Exit
\q
```

### 4.2 — Create the messages table

Connect to the new database:
```bash
psql -U bot_user -d telegram_bot_db
```

Create the table:
```sql
CREATE TABLE messages (
    id          SERIAL PRIMARY KEY,
    chat_id     BIGINT       NOT NULL,
    username    VARCHAR(255),
    text        TEXT,
    received_at TIMESTAMP    DEFAULT NOW()
);

\q
```

---

## Step 5 — Configure Environment Variables

Create a `.env` file in the project root:
```bash
touch .env
```

Add your secrets:
```ini
# .env
BOT_TOKEN=123456789:AAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
DATABASE_URL=postgresql://bot_user:yourpassword@localhost:5432/telegram_bot_db
WEBHOOK_URL=https://YOUR-NGROK-URL.ngrok.io
```

Add `.env` to `.gitignore` immediately:
```bash
echo ".env" >> .gitignore
```

---

## Step 6 — Write the Database Module

Delete the starter file and create your own:
```bash
rm hello.py
```

Create `db.py`:
```python
# db.py
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """Create and return a new database connection."""
    return psycopg2.connect(os.getenv("DATABASE_URL"))


def save_message(chat_id: int, username: str, text: str) -> None:
    """Save an incoming Telegram message to the database."""
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO messages (chat_id, username, text)
                    VALUES (%s, %s, %s)
                    """,
                    (chat_id, username, text),
                )
    finally:
        conn.close()
```

**What this does:**
- `get_connection()` — opens a connection to PostgreSQL using the URL from `.env`
- `save_message()` — inserts one row into the `messages` table
- The `with conn:` block handles transactions automatically (commits on success, rolls back on error)

---

## Alternative: File-Based Storage (if PostgreSQL is not available)

If you cannot install or run PostgreSQL, you can store messages in a local JSON file instead. This requires no external dependencies — Python's standard library handles everything.

This is suitable for learning and local testing. It is not recommended for production use because it does not support concurrent writes safely and has no query capabilities.

### Option A — JSON file

Replace the entire contents of `db.py` with the following:

```python
# db.py  (file-based version — JSON)
import json
import os
from datetime import datetime

STORAGE_FILE = "messages.json"


def _load() -> list:
    """Load all records from the JSON file. Return empty list if file does not exist."""
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(records: list) -> None:
    """Write all records back to the JSON file."""
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def save_message(chat_id: int, username: str, text: str) -> None:
    """Append one message record to the JSON file."""
    records = _load()
    records.append({
        "chat_id": chat_id,
        "username": username,
        "text": text,
        "received_at": datetime.now().isoformat(),
    })
    _save(records)


def read_messages() -> list:
    """Return all saved messages as a list of dicts."""
    return _load()
```

After the bot runs, a file named `messages.json` will appear in the project folder with content like:

```json
[
  {
    "chat_id": 12345678,
    "username": "YourName",
    "text": "/start",
    "received_at": "2024-01-15T10:23:45.123456"
  },
  {
    "chat_id": 12345678,
    "username": "YourName",
    "text": "hi",
    "received_at": "2024-01-15T10:23:50.456789"
  }
]
```

To read the file from the terminal:
```bash
# Print formatted output
python -c "import json; print(json.dumps(json.load(open('messages.json')), indent=2))"

# Count total messages
python -c "import json; print(len(json.load(open('messages.json'))))"
```

### Option B — CSV file

If you prefer a format that opens directly in Excel or a spreadsheet editor, use CSV:

```python
# db.py  (file-based version — CSV)
import csv
import os
from datetime import datetime

STORAGE_FILE = "messages.csv"
FIELDNAMES = ["chat_id", "username", "text", "received_at"]


def _ensure_file() -> None:
    """Create the CSV file with a header row if it does not exist."""
    if not os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def save_message(chat_id: int, username: str, text: str) -> None:
    """Append one message row to the CSV file."""
    _ensure_file()
    with open(STORAGE_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow({
            "chat_id": chat_id,
            "username": username,
            "text": text,
            "received_at": datetime.now().isoformat(),
        })


def read_messages() -> list:
    """Return all saved messages as a list of dicts."""
    _ensure_file()
    with open(STORAGE_FILE, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))
```

After the bot runs, `messages.csv` will look like:

```
chat_id,username,text,received_at
12345678,YourName,/start,2024-01-15T10:23:45.123456
12345678,YourName,hi,2024-01-15T10:23:50.456789
```

To read the file from the terminal:
```bash
# Print all rows
python -c "import csv; [print(r) for r in csv.DictReader(open('messages.csv'))]"
```

### No changes needed in `app.py`

Both file-based versions expose the same `save_message(chat_id, username, text)` function that `app.py` calls. You do not need to modify `app.py` at all — only swap out `db.py`.

### Comparison

| Feature | PostgreSQL | JSON file | CSV file |
|---------|-----------|-----------|----------|
| Setup required | Yes | None | None |
| Dependencies | psycopg2-binary | None | None |
| Concurrent writes | Safe | Unsafe | Unsafe |
| Human-readable | No | Yes | Yes |
| Opens in Excel | No | No | Yes |
| Suitable for production | Yes | No | No |

---

## Step 7 — Write the Flask Bot Application

Create `app.py`:
```python
# app.py
import os
import asyncio

from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv

import db

load_dotenv()

# -- Configuration ------------------------------------------------------------
BOT_TOKEN   = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

app = Flask(__name__)

bot = Bot(token=BOT_TOKEN)


# -- Command Handlers ---------------------------------------------------------

async def start_handler(update: Update, context) -> None:
    """/start — greet the user."""
    user = update.effective_user
    username = user.username or user.first_name

    db.save_message(
        chat_id=update.effective_chat.id,
        username=username,
        text=update.message.text,
    )

    await update.message.reply_text(
        f"Hello, World!\n\nNice to meet you, {username}."
    )


async def hello_handler(update: Update, context) -> None:
    """/hello — same greeting."""
    await start_handler(update, context)


async def echo_handler(update: Update, context) -> None:
    """Echo any plain text message back to the user."""
    user = update.effective_user
    username = user.username or user.first_name
    text = update.message.text

    db.save_message(
        chat_id=update.effective_chat.id,
        username=username,
        text=text,
    )

    await update.message.reply_text(f"You said: {text}")


# -- Build the Application ----------------------------------------------------

ptb_app = (
    Application.builder()
    .token(BOT_TOKEN)
    .build()
)

ptb_app.add_handler(CommandHandler("start", start_handler))
ptb_app.add_handler(CommandHandler("hello", hello_handler))
ptb_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_handler))


# -- Webhook Endpoint ---------------------------------------------------------

@app.route(f"/webhook/{BOT_TOKEN}", methods=["POST"])
def webhook():
    """Receive updates from Telegram and process them."""
    data = request.get_json(force=True)
    update = Update.de_json(data, bot)

    asyncio.run(ptb_app.process_update(update))

    return "OK", 200


# -- Health Check -------------------------------------------------------------

@app.route("/", methods=["GET"])
def index():
    return "Bot is running.", 200


# -- Register Webhook on Startup ----------------------------------------------

def register_webhook():
    """Tell Telegram where to send updates."""
    webhook_path = f"{WEBHOOK_URL}/webhook/{BOT_TOKEN}"
    asyncio.run(bot.set_webhook(url=webhook_path))
    print(f"Webhook registered: {webhook_path}")


if __name__ == "__main__":
    register_webhook()
    app.run(host="0.0.0.0", port=5000, debug=True)
```

---

## Step 8 — Expose Localhost with ngrok

Telegram requires a public HTTPS URL to deliver updates to your bot. During development, use ngrok to create a tunnel from the internet to your local machine.

### 8.1 — Install ngrok

Download from https://ngrok.com/download or:
```bash
# macOS (Homebrew)
brew install ngrok

# Linux (snap)
snap install ngrok
```

### 8.2 — Start the tunnel
```bash
ngrok http 5000
```

You will see output like:
```
Forwarding  https://abc123.ngrok.io -> http://localhost:5000
```

### 8.3 — Update your .env

Copy the `https://...ngrok.io` URL and update `.env`:
```ini
WEBHOOK_URL=https://abc123.ngrok.io
```

> Note: The ngrok URL changes every time you restart it on the free plan. Update `.env` each time.

---

## Step 9 — Run the Bot

```bash
uv run python app.py
```

Expected output:
```
Webhook registered: https://abc123.ngrok.io/webhook/123456789:AAF...
 * Running on http://0.0.0.0:5000
```

---

## Step 10 — Test Your Bot

1. Open Telegram
2. Search for your bot by its username (e.g. `@my_hello_world_bot`)
3. Press Start or send `/start`
4. The bot should respond:

```
Hello, World!

Nice to meet you, YourName.
```

5. Send any text message — the bot will echo it back.

---

## Step 11 — Verify the Database

Check that messages are being saved:
```bash
psql -U bot_user -d telegram_bot_db
```

```sql
SELECT * FROM messages;
```

Expected output:
```
 id | chat_id  | username | text   |       received_at
----+----------+----------+--------+--------------------------
  1 | 12345678 | YourName | /start | 2024-01-15 10:23:45.123
  2 | 12345678 | YourName | hi     | 2024-01-15 10:23:50.456
```

---

## Complete File Reference

### `pyproject.toml` (auto-generated by uv)
```toml
[project]
name = "telegram-bot"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "flask>=3.0.0",
    "python-telegram-bot>=21.0",
    "psycopg2-binary>=2.9.9",
    "python-dotenv>=1.0.0",
]
```

### `.env`
```ini
BOT_TOKEN=123456789:AAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
DATABASE_URL=postgresql://bot_user:yourpassword@localhost:5432/telegram_bot_db
WEBHOOK_URL=https://YOUR-NGROK-URL.ngrok.io
```

### `db.py`
*(See Step 6)*

### `app.py`
*(See Step 7)*

---

## Daily Workflow

Every time you work on the project:

```bash
# 1. Start PostgreSQL (if not running as a service)
pg_ctl start

# 2. Start ngrok
ngrok http 5000
# Copy the new HTTPS URL to .env -> WEBHOOK_URL=...

# 3. Run the bot
uv run python app.py
```

---

## Common Errors and Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `telegram.error.InvalidToken` | Wrong or missing BOT_TOKEN | Check `.env`, no spaces around `=` |
| `psycopg2.OperationalError` | Cannot connect to Postgres | Check `DATABASE_URL`, ensure Postgres is running |
| `400 Bad Request: bad webhook` | ngrok URL is HTTP, not HTTPS | Make sure `WEBHOOK_URL` starts with `https://` |
| `conflict: terminated by other getUpdates request` | Two instances running | Stop all other instances, restart once |
| Webhook not receiving updates | ngrok restarted, URL changed | Update `WEBHOOK_URL` in `.env` and restart app |

---

## Next Steps

Once the bot is working, consider the following extensions:

- Add an `/about` command that describes the bot
- Add a `/history` command that retrieves the last 5 messages from the database
- Add an inline keyboard with buttons
- Deploy to a cloud server (Render, Railway, or a VPS) to remove the dependency on ngrok
- Use server environment variables in production instead of a `.env` file

---

## References

- python-telegram-bot documentation: https://docs.python-telegram-bot.org/
- uv documentation: https://docs.astral.sh/uv/
- Flask documentation: https://flask.palletsprojects.com/
- psycopg2 documentation: https://www.psycopg.org/docs/
- Telegram Bot API: https://core.telegram.org/bots/api
