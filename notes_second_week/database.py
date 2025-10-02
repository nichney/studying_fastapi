import sqlite3
import asyncio
from typing import Tuple, Optional

class Query:
    def __init__(self, db_path: str = "notes.db"):
        self.db_path = db_path
        self._lock = asyncio.Lock()  
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY
        )
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            user_id INTEGER,
            note_id INTEGER,
            note_date TEXT,
            note_text TEXT,
            PRIMARY KEY (user_id, note_id),
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
        """)
        conn.commit()
        conn.close()

    async def new_note(self, user_id: int, note_text: str, note_date: str) -> int:
        async with self._lock:
            return await asyncio.to_thread(self._new_note_sync, user_id, note_text, note_date)

    def _new_note_sync(self, user_id: int, note_text: str, note_date: str) -> int:
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        # ensure user exists
        cur.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
        if not cur.fetchone():
            raise ValueError(f"User {user_id} does not exist")

        # find last note_id
        cur.execute("SELECT MAX(note_id) FROM notes WHERE user_id = ?", (user_id,))
        row = cur.fetchone()
        last_id = row[0] if row and row[0] is not None else 0
        new_id = last_id + 1

        # 3) add new note
        cur.execute(
            "INSERT INTO notes (user_id, note_id, note_date, note_text) VALUES (?, ?, ?, ?)",
            (user_id, new_id, note_date, note_text)
        )

        conn.commit()
        conn.close()
        return new_id

    async def get_note(self, user_id: int, note_id: int) -> Tuple[str, str]:
        async with self._lock:
            return await asyncio.to_thread(self._get_note_sync, user_id, note_id)

    def _get_note_sync(self, user_id: int, note_id: int) -> Tuple[str, str]:
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        # ensure user exists
        cur.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
        if not cur.fetchone():
            raise ValueError(f"User {user_id} does not exist")

        # ensure note_id exists
        cur.execute("SELECT note_date, note_text FROM notes WHERE user_id = ? AND note_id = ?", (user_id, note_id))
        row = cur.fetchone()
        if not row:
            raise ValueError(f"Note {note_id} does not exist for user {user_id}")

        conn.close()
        return row  # (note_date, note_text)

    async def delete_note(self, user_id: int, note_id: int) -> bool:
        async with self._lock:
            return await asyncio.to_thread(self._delete_note_sync, user_id, note_id)

    def _delete_note_sync(self, user_id: int, note_id: int) -> bool:
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        # ensure user exists
        cur.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
        if not cur.fetchone():
            raise ValueError(f"User {user_id} does not exist")

        # ensure note_id exists
        cur.execute("SELECT 1 FROM notes WHERE user_id = ? AND note_id = ?", (user_id, note_id))
        if not cur.fetchone():
            raise ValueError(f"Note {note_id} does not exist for user {user_id}")

        cur.execute("DELETE FROM notes WHERE user_id = ? AND note_id = ?", (user_id, note_id))
        conn.commit()
        conn.close()
        return True

    async def ensure_user(self, user_id: int):
        """Creates user if there is no user"""
        async with self._lock:
            return await asyncio.to_thread(self._ensure_user_sync, user_id)

    def _ensure_user_sync(self, user_id: int):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
        conn.commit()
        conn.close()


