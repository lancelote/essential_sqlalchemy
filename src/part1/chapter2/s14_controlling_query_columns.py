from sqlalchemy import select

from src.part1.chapter2.s13_result_proxy import cookies, connection

selection = select([cookies.c.cookie_name, cookies.c.quantity])
result_proxy = connection.execute(selection)
assert result_proxy.keys() == ['cookie_name', 'quantity']  # List of columns

result = result_proxy.first()
assert result == ('chocolate chip', 12)
