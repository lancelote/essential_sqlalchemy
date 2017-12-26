from sqlalchemy import select, desc

from src.part1.chapter2.controlling_query_columns import cookies, connection

selection = select([cookies.c.cookie_name, cookies.c.quantity])
selection = selection.order_by(desc(cookies.c.quantity))
result_proxy = connection.execute(selection)

assert result_proxy.fetchall() == [
    ('oatmeal raisin', 100),
    ('peanut butter', 24),
    ('chocolate chip', 12),
    ('dark chocolate chip', 1)
]
