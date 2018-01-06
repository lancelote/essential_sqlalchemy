from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError

from src.part1.chapter3.s30_attribute_error import connection, users

selection = select([users.c.username])
result = connection.execute(selection).fetchall()
assert result == [('cookiemon',)]

insertion = insert(users).values(
    username='cookiemon',
    email_address='damon@cookie.com',
    phone='111-111-1111',
    password='password'
)
try:
    connection.execute(insertion)
except IntegrityError:
    pass
else:
    raise AssertionError('Should raise IntegrityError')
