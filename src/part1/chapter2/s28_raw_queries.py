from sqlalchemy import select, text

from src.part1.chapter2.s27_chaining import connection, users

# noinspection SqlNoDataSourceInspection
result = connection.execute('SELECT * FROM orders').fetchall()
assert result == [(1, 1, 0), (2, 2, 0)]

stmt = select([users]).where(text("username='cookiemon'"))
# print(connection.execute(stmt).fetchall())
# [
#     (1, 'cookiemon', 'mon@cookie.com', '111-111-1111', 'password',
#      datetime.datetime(2018, 1, 3, 21, 24, 42, 928133),
#      datetime.datetime(2018, 1, 3, 21, 24, 42, 928141))
# ]
