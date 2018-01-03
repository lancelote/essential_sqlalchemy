from sqlalchemy import insert

from src.part1.chapter1.in_memory_full_example import users, orders, line_items
from src.part1.chapter2.deleting import connection

customer_list = [
    {
        'username': 'cookiemon',
        'email_address': 'mon@cookie.com',
        'phone': '111-111-1111',
        'password': 'password',
    },
    {
        'username': 'cakeeater',
        'email_address': 'cakeeater@cake.com',
        'phone': '222-222-2222',
        'password': 'password',
    },
    {
        'username': 'pieguy',
        'email_address': 'guy@pie.com',
        'phone': '333-333-3333',
        'password': 'password',
    }
]
insertion = users.insert()
connection.execute(insertion, customer_list)

insertion = insert(orders).values(user_id=1, order_id=1)
connection.execute(insertion)

insertion = insert(line_items)
order_items = [
    {
        'order_id': 1,
        'cookie_id': 1,
        'quantity': 2,
        'extended_cost': 1.00
    },
    {
        'order_id': 1,
        'cookie_id': 3,
        'quantity': 12,
        'extended_cost': 3.00
    }
]
connection.execute(insertion, order_items)

insertion = insert(orders).values(user_id=2, order_id=2)
connection.execute(insertion)

insertion = insert(line_items)
order_items = [
    {
        'order_id': 2,
        'cookie_id': 1,
        'quantity': 24,
        'extended_cost': 12.00,
    },
    {
        'order_id': 2,
        'cookie_id': 4,
        'quantity': 6,
        'extended_cost': 6.00,
    }
]
connection.execute(insertion, order_items)
