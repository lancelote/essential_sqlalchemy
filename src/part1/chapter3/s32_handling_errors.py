from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError

from src.part1.chapter3.s31_integrity_error import connection, users

insertion = insert(users).values(
    username='cookiemon',
    email_address='damon@cookie.com',
    phone='111-111-1111',
    password='password'
)
try:
    result = connection.execute(insertion)
except IntegrityError as error:
    assert str(error.orig) == 'UNIQUE constraint failed: users.username'
