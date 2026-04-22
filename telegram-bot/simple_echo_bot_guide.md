# Simple Echo Bot
### Python · uv · OOP · JSON Storage — Step-by-Step Guide for Students

---

## What the Bot Does

The bot echoes every message back to the sender:

```
User:  Hello
Bot:   You said: Hello

User:  How are you?
Bot:   You said: How are you?
```

There is no Flask, no webhooks, and no database server. The bot runs with polling — it asks Telegram for new messages every few seconds — and saves all conversations to a local JSON file. No external services are required beyond Telegram itself.

---

## Project Structure

```
simple-echo-bot/
├── .env
├── .python-version
├── pyproject.toml
├── storage.py
├── bot.py
└── main.py
```

Each file has a single responsibility:

- `storage.py` — reads and writes messages to a JSON file
- `bot.py` — contains the bot logic as a class
- `main.py` — entry point, starts the bot

---

## Step 1 — Create the Project

```bash
uv init simple-echo-bot
cd simple-echo-bot
uv python pin 3.11
```

This creates `pyproject.toml`, `.python-version`, and a starter `hello.py` which you will delete in Step 4.

---

## Step 2 — Add Dependencies

This bot only needs two packages:

```bash
uv add python-telegram-bot python-dotenv
```

No `psycopg2`, no `flask`. The `json` module used for storage is part of Python's standard library and requires no installation.

---

## Step 3 — Create the Bot on Telegram

1. Open Telegram and find **@BotFather**
2. Send `/newbot`
3. Choose a name: e.g. `Echo Bot`
4. Choose a username (must end in `bot`): e.g. `my_echo_bot`
5. Copy the token you receive — it looks like:

```
123456789:AAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> **Important:** Keep this token secret. Never commit it to Git.

---

## Step 4 — Configure the Environment

Delete the starter file and create `.env`:

```bash
rm hello.py
touch .env
echo ".env" >> .gitignore
```

Add your token to `.env`:

```ini
BOT_TOKEN=123456789:AAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Step 5 — Write the Storage Class

Create `storage.py`:

```python
# storage.py
import json
import os
from datetime import datetime


class JsonStorage:
    """Saves and retrieves messages from a local JSON file."""

    def __init__(self, filepath: str = "messages.json"):
        self.filepath = filepath
        self._ensure_file()

    def _ensure_file(self) -> None:
        """Create an empty JSON array if the file does not exist."""
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump([], f)

    def save(self, chat_id: int, username: str, text: str) -> None:
        """Append one message record to the file."""
        records = self.load_all()
        records.append({
            "chat_id": chat_id,
            "username": username,
            "text": text,
            "received_at": datetime.now().isoformat(),
        })
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)

    def load_all(self) -> list:
        """Return all records as a list of dicts."""
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def count(self) -> int:
        """Return the total number of saved messages."""
        return len(self.load_all())
```

**Method breakdown:**

- `__init__` — receives the file path and calls `_ensure_file` so the file always exists before any read or write
- `_ensure_file` — creates the file with an empty JSON array `[]` if it is missing
- `save` — loads all existing records, appends the new one, and writes everything back
- `load_all` — reads the file and returns the full list
- `count` — returns the total number of stored messages

---

## Step 6 — Write the Bot Class

Create `bot.py`:

```python
# bot.py
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from storage import JsonStorage

load_dotenv()


class EchoBot:
    """A Telegram bot that echoes every text message back to the sender."""

    def __init__(self):
        self.token = os.getenv("BOT_TOKEN")
        self.storage = JsonStorage()
        self.app = Application.builder().token(self.token).build()
        self._register_handlers()

    def _register_handlers(self) -> None:
        """Attach command and message handlers to the application."""
        self.app.add_handler(CommandHandler("start", self._handle_start))
        self.app.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message)
        )

    async def _handle_start(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        """/start — introduce the bot."""
        username = update.effective_user.username or update.effective_user.first_name
        self.storage.save(
            chat_id=update.effective_chat.id,
            username=username,
            text=update.message.text,
        )
        await update.message.reply_text(
            "Bot is running. Send any message and it will be echoed back."
        )

    async def _handle_message(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        """Echo any plain text message back to the sender and save it."""
        username = update.effective_user.username or update.effective_user.first_name
        text = update.message.text

        self.storage.save(
            chat_id=update.effective_chat.id,
            username=username,
            text=text,
        )

        await update.message.reply_text(f"You said: {text}")

    def run(self) -> None:
        """Start the bot using long polling."""
        print(f"Bot started. Messages are saved to: {self.storage.filepath}")
        print("Press Ctrl+C to stop.")
        self.app.run_polling()
```

**Method breakdown:**

- `__init__` — loads the token from `.env`, creates a `JsonStorage` instance, builds the Telegram `Application`, and calls `_register_handlers`
- `_register_handlers` — connects `/start` and plain text messages to their handler methods
- `_handle_start` — responds when the user opens the bot with `/start`
- `_handle_message` — saves the incoming message and replies with `You said: <text>`
- `run` — starts the polling loop, which keeps the bot alive until you press Ctrl+C

---

## Step 7 — Write the Entry Point

Create `main.py`:

```python
# main.py
from bot import EchoBot


def main():
    bot = EchoBot()
    bot.run()


if __name__ == "__main__":
    main()
```

This file only does one thing: create the bot and start it. All logic lives in `bot.py` and `storage.py`.

---

## Step 8 — Run the Bot

```bash
uv run python main.py
```

Expected output:

```
Bot started. Messages are saved to: messages.json
Press Ctrl+C to stop.
```

Open Telegram, find your bot, and send a message:

```
You:  Hello
Bot:  You said: Hello

You:  Good morning
Bot:  You said: Good morning
```

To stop the bot, press **Ctrl+C** in the terminal.

---

## Step 9 — Inspect the Saved Messages

While the bot is running or after stopping it, read `messages.json` from the terminal:

```bash
python -c "import json; print(json.dumps(json.load(open('messages.json')), indent=2))"
```

Example output:

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
    "text": "Hello",
    "received_at": "2024-01-15T10:23:50.456789"
  },
  {
    "chat_id": 12345678,
    "username": "YourName",
    "text": "Good morning",
    "received_at": "2024-01-15T10:23:55.789012"
  }
]
```

To count how many messages have been saved:

```bash
python -c "from storage import JsonStorage; print(JsonStorage().count())"
```

---

## Complete File Reference

### `pyproject.toml`
```toml
[project]
name = "simple-echo-bot"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "python-telegram-bot>=21.0",
    "python-dotenv>=1.0.0",
]
```

### `.env`
```ini
BOT_TOKEN=123456789:AAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### `storage.py`
*(See Step 5)*

### `bot.py`
*(See Step 6)*

### `main.py`
*(See Step 7)*

---

## How Polling Works

This bot uses **polling**: every few seconds it sends a request to Telegram asking "are there any new messages?". Telegram responds with a list of updates, the bot processes them, and then asks again.

This is different from webhooks, where Telegram calls your server the moment a message arrives. Polling is simpler to set up because it requires no public URL and no web server — it works on any machine with internet access.

| | Polling | Webhooks |
|--|---------|----------|
| Requires public URL | No | Yes |
| Requires ngrok in dev | No | Yes |
| Setup complexity | Low | Higher |
| Suitable for production | Yes, for small bots | Yes |
| Response speed | Up to ~1 second delay | Instant |

For learning and small projects, polling is the right choice. For production bots with high message volume, webhooks are preferred.

---

## Common Errors and Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `telegram.error.InvalidToken` | Wrong token in `.env` | Check for extra spaces or missing characters in the token |
| `json.decoder.JSONDecodeError` | `messages.json` was manually edited and is malformed | Delete `messages.json` and restart — the file will be recreated automatically |
| Bot does not respond to messages | `run_polling()` was not called | Make sure `bot.run()` is called in `main.py` |
| `KeyError: 'BOT_TOKEN'` | `.env` file is missing or not loaded | Check that `.env` exists in the project root and contains `BOT_TOKEN=...` |

---

## References

- python-telegram-bot documentation: https://docs.python-telegram-bot.org/
- uv documentation: https://docs.astral.sh/uv/
- Telegram Bot API: https://core.telegram.org/bots/api
