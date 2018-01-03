from sqlalchemy import func, select

from src.part1.chapter2.s24_joining import connection, orders, users

columns = [users.c.username, func.count(orders.c.order_id)]
all_orders = select(columns)
all_orders = all_orders.select_from(users.outerjoin(orders))
all_orders = all_orders.group_by(users.c.username)
result = connection.execute(all_orders).fetchall()
assert result == [
    ('cakeeater', 1),
    ('cookiemon', 1),
    ('pieguy', 0)
]
