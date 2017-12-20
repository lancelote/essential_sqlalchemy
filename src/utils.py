import os
import sqlite3

ROOT = os.path.join(os.path.dirname(__file__), '..')


def create_sqlite_db(name: str):
    """Create sqlite3 database inside dbs folder."""
    connection = sqlite3.connect(f'{ROOT}/dbs/{name}')
    connection.close()
