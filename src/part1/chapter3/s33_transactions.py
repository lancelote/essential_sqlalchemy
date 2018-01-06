from sqlalchemy import insert, select, update
from sqlalchemy.exc import IntegrityError

from src.part1.chapter3.s29_exceptions import connection, cookies, line_items, orders, users

# Defining the stock #
######################

insertion = insert(users).values(
    username='cookiemon',
    email_address='mon@cookie.com',
    phone='111-111-1111',
    password='password')
connection.execute(insertion)

insertion = cookies.insert()
inventory_list = [
    {
        'cookie_name': 'chocolate chip',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe.html',
        'cookie_sku': 'CC01',
        'quantity': '12',
        'unit_cost': '0.50'
    },
    {
        'cookie_name': 'dark chocolate chip',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe_dark.html',
        'cookie_sku': 'CC02',
        'quantity': '1',
        'unit_cost': '0.75'
    }]
connection.execute(insertion, inventory_list)

# Adding orders for user #
##########################

insertion = insert(orders).values(user_id=1, order_id='1')
connection.execute(insertion)

insertion = insert(line_items)
order_items = [
    {
        'order_id': 1,
        'cookie_id': 1,
        'quantity': 9,
        'extended_cost': 4.50
    }]
connection.execute(insertion, order_items)

insertion = insert(orders).values(user_id=1, order_id='2')
connection.execute(insertion)

insertion = insert(line_items)
order_items = [
    {
        'order_id': 2,
        'cookie_id': 1,
        'quantity': 4,
        'extended_cost': 1.50
    },
    {
        'order_id': 2,
        'cookie_id': 2,
        'quantity': 1,
        'extended_cost': 4.50
    }]
connection.execute(insertion, order_items)


# Executing orders #
####################


def ship_id(order_id):
    """Ship given order."""
    ordered_cookies = select([line_items.c.cookie_id, line_items.c.quantity])
    ordered_cookies = ordered_cookies.where(line_items.c.order_id == order_id)
    cookies_to_ship = connection.execute(ordered_cookies)
    for cookie in cookies_to_ship:
        updating = update(cookies).where(cookies.c.cookie_id == cookie.cookie_id)
        updating = updating.values(quantity=cookies.c.quantity - cookie.quantity)
        connection.execute(updating)
    shipping = update(orders).where(orders.c.order_id == order_id)
    shipping = shipping.values(shipped=True)
    connection.execute(shipping)


ship_id(1)
selection = select([cookies.c.cookie_name, cookies.c.quantity])
result = connection.execute(selection).fetchall()
assert result == [('chocolate chip', 3), ('dark chocolate chip', 1)]

try:
    ship_id(2)
except IntegrityError:
    pass
else:
    raise AssertionError('Should raise IntegrityError')


def safe_ship_it(order_id):
    """Ship given order or roll back in case of an error."""
    ordered_cookies = select([line_items.c.cookie_id, line_items.c.quantity])
    ordered_cookies = ordered_cookies.where(line_items.c.order_id == order_id)
    transaction = connection.begin()
    cookies_to_ship = connection.execute(ordered_cookies).fetchall()

    try:
        for cookie in cookies_to_ship:
            updating = update(cookies).where(cookies.c.cookie_id == cookie.cookie_id)
            updating = updating.values(quantity=cookies.c.quantity - cookie.quantity)
            connection.execute(updating)
        shipping = update(orders).where(orders.c.order_id == order_id)
        shipping = shipping.values(shipped=True)
        connection.execute(shipping)
        transaction.commit()
        return 0
    except IntegrityError:
        transaction.rollback()
        return 1


# Restore dark chocolate chip cookies quantity
selection = update(cookies).where(cookies.c.cookie_name == 'dark chocolate chip')
selection = selection.values(quantity=1)
connection.execute(selection)

selection = select([cookies.c.cookie_name, cookies.c.quantity])
result = connection.execute(selection).fetchall()
assert result == [('chocolate chip', 3), ('dark chocolate chip', 1)]

# Try failing shipment
assert safe_ship_it(2) == 1

# Cookies quantity wasn't altered
selection = select([cookies.c.cookie_name, cookies.c.quantity])
result = connection.execute(selection).fetchall()
assert result == [('chocolate chip', 3), ('dark chocolate chip', 1)]
