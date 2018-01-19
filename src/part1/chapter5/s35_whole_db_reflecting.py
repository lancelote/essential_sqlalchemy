from sqlalchemy import MetaData, create_engine

metadata = MetaData()
engine = create_engine('sqlite:///../../../dbs/Chinook_Sqlite.sqlite')
metadata.reflect(bind=engine)

assert 'Employee' in metadata.tables.keys()
