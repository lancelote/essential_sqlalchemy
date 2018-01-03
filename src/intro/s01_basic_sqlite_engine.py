from sqlalchemy import create_engine

from src.utils import create_sqlite_db, ROOT

NAME = 'cookies.db'
create_sqlite_db(NAME)

engine0 = create_engine(f'sqlite:///dbs/{NAME}')  # Relative directory
engine1 = create_engine('sqlite:///:memory:')  # In-memory
engine2 = create_engine(f'sqlite:///{ROOT}/dbs/{NAME}')  # Absolute path UNIX
engine3 = create_engine(f'sqlite:///c:\\dbs\\{NAME}')  # Absolute path Win

# create_engine doesn't initiate a connection, only engine is created
# connection is going to be established when some action'll require it
engine2.connect().close()
