import os
import sqlite3
import re

ROOT = os.path.join(os.path.dirname(__file__), '..')
FILE_MASK = r'_(\d{2}_.+)'
REPLACE_WITH = r's\1'


def create_sqlite_db(name: str):
    """Create sqlite3 database inside dbs folder."""
    folder = os.path.join(ROOT, 'dbs')
    if not os.path.exists(folder):
        os.makedirs(folder)
    connection = sqlite3.connect(f'{folder}/{name}')
    connection.close()


def rename_note_files(pattern=FILE_MASK, repl=REPLACE_WITH):
    for root, _, files in os.walk(os.path.join(ROOT, 'src')):
        for file in files:
            new_name = re.sub(pattern, repl, file)
            os.renames(root + os.sep + file, root + os.sep + new_name)


if __name__ == '__main__':
    rename_note_files()
