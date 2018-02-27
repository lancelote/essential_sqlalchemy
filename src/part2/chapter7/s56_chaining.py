from decimal import Decimal

from src.part2.chapter7.s54_joins import Cookie, LineItem
from src.part2.chapter7.s55_grouping import Order, User, session


# %% Get all orders by the customer
def get_orders_by_customer(customer_name):
    query = session.query(
        Order.order_id,
        User.username,
        User.phone,
        Cookie.cookie_name,
        LineItem.quantity,
        LineItem.extended_cost
    )
    query = query.join(User).join(LineItem).join(Cookie)
    results = query.filter(User.username == customer_name).all()
    return results


assert get_orders_by_customer('cakeeater') == [
    (2, 'cakeeater', '222-222-2222', 'chocolate chip', 24, Decimal('12.00')),
    (2, 'cakeeater', '222-222-2222', 'oatmeal raisin', 6, Decimal('6.00'))
]


# %% Specify shipped status and details flag
def get_orders_by_customer(customer_name, shipped=None, details=False):
    query = session.query(Order.order_id, User.username, User.phone)
    query = query.join(User)
    if details:
        query = query.add_columns(Cookie.cookie_name, LineItem.quantity, LineItem.extended_cost)
        query = query.join(LineItem).join(Cookie)
    if shipped is not None:
        query = query.filter(Order.shipped == shipped)
    results = query.filter(User.username == customer_name).all()
    return results


# %% Get all orders
assert get_orders_by_customer('cakeeater') == [(2, 'cakeeater', '222-222-2222')]

# %% Get all orders with details
assert get_orders_by_customer('cakeeater', details=True) == [
    (2, 'cakeeater', '222-222-2222', 'chocolate chip', 24, Decimal('12.00')),
    (2, 'cakeeater', '222-222-2222', 'oatmeal raisin', 6, Decimal('6.00'))
]

# %% Get only orders that have shipped
assert get_orders_by_customer('cakeeater', shipped=True) == []

# %% Get orders that haven't shipped yet
assert get_orders_by_customer('cakeeater', shipped=False) == [(2, 'cakeeater', '222-222-2222')]

# %% Get orders that haven't shipped yet with details
assert get_orders_by_customer('cakeeater', shipped=False, details=True) == [
    (2, 'cakeeater', '222-222-2222', 'chocolate chip', 24, Decimal('12.00')),
    (2, 'cakeeater', '222-222-2222', 'oatmeal raisin', 6, Decimal('6.00'))
]
