import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parent.parent.parent / "database.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection