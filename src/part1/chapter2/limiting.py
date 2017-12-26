from sqlalchemy import select

from src.part1.chapter2.ordering import cookies, connection

selection = select([cookies.c.cookie_name, cookies.c.quantity])
selection = selection.order_by(cookies.c.quantity)
selection = selection.limit(2)

result_proxy = connection.execute(selection)
assert [result.cookie_name for result in result_proxy] == ['dark chocolate chip', 'chocolate chip']
