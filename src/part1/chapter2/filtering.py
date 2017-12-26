from sqlalchemy import select

from src.part1.chapter2.sql_functions_and_labels import cookies, connection

# Finding chocolate chip
selection = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')
result_proxy = connection.execute(selection)
record = result_proxy.first()
assert record.cookie_name == 'chocolate chip'

# Finding names with chocolate in them
selection = select([cookies]).where(cookies.c.cookie_name.like('%chocolate%'))
result_proxy = connection.execute(selection)
records = result_proxy.fetchall()
assert [record.cookie_name for record in records] == ['chocolate chip', 'dark chocolate chip']
