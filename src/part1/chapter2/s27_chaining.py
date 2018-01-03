from decimal import Decimal

from sqlalchemy import select

from src.part1.chapter2.s24_joining import cookies, line_items
from src.part1.chapter2.s26_grouping import connection, orders, users


def get_orders_by_customer0(customer_name):
    """Get all orders of the given customer."""
    columns = [
        orders.c.order_id,
        users.c.username,
        users.c.phone,
        cookies.c.cookie_name,
        line_items.c.quantity,
        line_items.c.extended_cost
    ]
    customer_orders = select(columns)
    customer_orders = customer_orders.select_from(
        users.join(orders).join(line_items).join(cookies))
    customer_orders = customer_orders.where(users.c.username == customer_name)
    result = connection.execute(customer_orders).fetchall()
    return result


assert get_orders_by_customer0('cakeeater') == [
    (2, 'cakeeater', '222-222-2222', 'chocolate chip', 24, Decimal('12.00')),
    (2, 'cakeeater', '222-222-2222', 'oatmeal raisin', 6, Decimal('6.00'))
]


def get_orders_by_customer1(customer_name, shipped=None, details=False):
    """Get all orders of the given customer.

    Args:
        customer_name (str): Customer name
        shipped (bool): Specify if orders are already shipped
        details (bool): Provide more details about the order
    """
    columns = [
        orders.c.order_id,
        users.c.username,
        users.c.phone,
    ]
    joins = users.join(orders)
    if details:
        columns.extend([
            cookies.c.cookie_name,
            line_items.c.quantity,
            line_items.c.extended_cost
        ])
        joins = joins.join(line_items).join(cookies)
    customer_orders = select(columns)
    customer_orders = customer_orders.select_from(joins)
    customer_orders = customer_orders.where(users.c.username == customer_name)
    if shipped is not None:
        customer_orders = customer_orders.where(orders.c.shipped == shipped)
    result = connection.execute(customer_orders).fetchall()
    return result


# Get all orders
assert get_orders_by_customer1('cakeeater') == [
    (2, 'cakeeater', '222-222-2222')
]

# Get all orders with details
assert get_orders_by_customer1('cakeeater', details=True) == [
    (2, 'cakeeater', '222-222-2222', 'chocolate chip', 24, Decimal('12.00')),
    (2, 'cakeeater', '222-222-2222', 'oatmeal raisin', 6, Decimal('6.00')),
]

# Get only orders that have shipped
assert get_orders_by_customer1('cakeeater', shipped=True) == []

# Get orders that haven't shipped yet
assert get_orders_by_customer1('cakeeater', shipped=False) == [
    (2, 'cakeeater', '222-222-2222')
]

# Get orders that haven't shipped yet with details
assert get_orders_by_customer1('cakeeater', shipped=False, details=True) == [
    (2, 'cakeeater', '222-222-2222', 'chocolate chip', 24, Decimal('12.00')),
    (2, 'cakeeater', '222-222-2222', 'oatmeal raisin', 6, Decimal('6.00')),
]
