from sqlalchemy import select, func

from src.part1.chapter2.additional_data import orders, users, connection, line_items
from src.part1.chapter2.deleting import cookies

columns = [
    orders.c.order_id,
    users.c.username,
    users.c.phone,
    cookies.c.cookie_name,
    line_items.c.quantity,
    line_items.c.extended_cost,
]
cookiemon_orders = select(columns)
cookiemon_orders = cookiemon_orders.select_from(
    orders.join(users).join(line_items).join(cookies)).where(
    users.c.username == 'cookiemon')
result = connection.execute(cookiemon_orders).fetchall()
assert len(result) == 2

# for row in result:
#     print(row)
# (1, 'cookiemon', '111-111-1111', 'chocolate chip', 2, Decimal('1.00'))
# (1, 'cookiemon', '111-111-1111', 'peanut butter', 12, Decimal('3.00'))

columns = [users.c.username, func.count(orders.c.order_id)]
all_orders = select(columns)
all_orders = all_orders.select_from(users.outerjoin(orders))
all_orders = all_orders.group_by(users.c.username)
result = connection.execute(all_orders).fetchall()
assert len(result) == 3

# for row in result:
#     print(row)
# ('cakeeater', 1)
# ('cookiemon', 1)
# ('pieguy', 0)
