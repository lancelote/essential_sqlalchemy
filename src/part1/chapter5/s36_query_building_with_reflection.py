from sqlalchemy import select

from src.part1.chapter5.s35_whole_db_reflecting import engine, metadata

playlist = metadata.tables['Playlist']
selection = select([playlist]).limit(10)
first_10_records = engine.execute(selection).fetchall()

assert (1, 'Music') in first_10_records
