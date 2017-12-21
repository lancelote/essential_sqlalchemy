import os
import sqlite3

ROOT = os.path.join(os.path.dirname(__file__), '..')


def create_sqlite_db(name: str):
    """Create sqlite3 database inside dbs folder."""
    folder = os.path.join(ROOT, 'dbs')
    if not os.path.exists(folder):
        os.makedirs(folder)
    connection = sqlite3.connect(f'{folder}/{name}')
    connection.close()
