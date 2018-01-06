from sqlalchemy import insert, select

from src.part1.chapter3.s29_exceptions import connection, users

insertion = insert(users).values(
    username='cookiemon',
    email_address='mon@cookie.com',
    phone='111-111-1111',
    password='password'
)
connection.execute(insertion)

selection = select([users.c.username])
results = connection.execute(selection)
record = results.first()
try:
    print(record.password)
except AttributeError:
    pass
else:
    raise AssertionError('Expected to raise AttributeError')
