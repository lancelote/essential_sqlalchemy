from sqlalchemy.exc import IntegrityError, InvalidRequestError

from src.part2.chapter8.s62_db_setup_for_transactions import Cookie, LineItem, Order, User, session

# Transaction example #
#######################

cookiemon = User('cookiemon', 'mon@cookie.com', '111-111-1111', 'password')
cc = Cookie('chocolate chip', 'http://some.aweso.me/cookie/recipe.html', 'CC01', 12, 0.50)
dcc = Cookie('dark chocolate chip', 'http://some.aweso.me/cookie/recipe_dark.html', 'CC02', 1, 0.75)

session.add(cookiemon)
session.add(cc)
session.add(dcc)

# Add first order
o1 = Order()
o1.user = cookiemon
session.add(o1)

line1 = LineItem(order=o1, cookie=cc, quantity=9, extended_cost=4.50)

session.add(line1)
session.commit()

# Add second order
o2 = Order()
o2.user = cookiemon
session.add(o2)

line1 = LineItem(order=o2, cookie=cc, quantity=2, extended_cost=1.50)
line2 = LineItem(order=o2, cookie=dcc, quantity=9, extended_cost=6.75)

session.add(line1)
session.add(line2)
session.commit()


def ship_it(order_id):
    order = session.query(Order).get(order_id)
    for li in order.line_items:
        li.cookie.quantity = li.cookie.quantity - li.quantity
        session.add(li.cookie)
    order.shipped = True
    session.add(order)
    session.commit()
    return 'shipped order ID: {}'.format(order_id)


result = ship_it(1)
assert result == 'shipped order ID: 1'
assert session.query(Cookie.cookie_name, Cookie.quantity).all() == [('chocolate chip', 3), ('dark chocolate chip', 1)]

try:
    ship_it(2)
except IntegrityError:
    pass
else:
    raise AssertionError('Should raise IntegrityError')

# Query on an failed session
try:
    session.query(Cookie.cookie_name, Cookie.quantity).all()
except InvalidRequestError:
    pass
else:
    raise AssertionError('Should raise InvalidRequestError')

# Rollback to restore the session
session.rollback()
assert session.query(Cookie.cookie_name, Cookie.quantity).all() == [('chocolate chip', 3), ('dark chocolate chip', 1)]


def safe_ship_it(order_id):
    order = session.query(Order).get(order_id)
    for li in order.line_items:
        li.cookie.quantity = li.cookie.quantity - li.quantity
        session.add(li.cookie)
    order.shipped = True
    session.add(order)
    try:
        session.commit()
        return 'Shipped order ID: {}'.format(order_id)
    except IntegrityError as error:
        session.rollback()
        return 'Error: {!s}'.format(error.orig)


result = safe_ship_it(2)
assert result == 'Error: CHECK constraint failed: quantity_positive'
assert session.query(Cookie.cookie_name, Cookie.quantity).all() == [('chocolate chip', 3), ('dark chocolate chip', 1)]
