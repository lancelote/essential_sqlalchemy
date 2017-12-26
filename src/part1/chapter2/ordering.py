from sqlalchemy import select

from src.part1.chapter2.controlling_query_columns import cookies, connection

selection = select([cookies.c.cookie_name, cookies.c.quantity])
selection = selection.order_by(cookies)
result_proxy = connection.execute(selection)
assert result_proxy.fetchall() == [
    ('chocolate chip', 12), ('dark chocolate chip', 1),
    ('peanut butter', 24), ('oatmeal raisin', 100)]
