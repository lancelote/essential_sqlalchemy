from src.part2.chapter7.s41_session import Cookie, LineItem, Order, User
from src.part2.chapter7.s52_deleting_data import session

# %% Users
cookiemon = User(
    username='cookiemon',
    email_address='mon@cookie.com',
    phone='111-111-1111',
    password='password'
)
cakeeater = User(
    username='cakeeater',
    email_address='cakeeater@cake.com',
    phone='222-222-2222',
    password='password'
)
pieperson = User(
    username='pieperson',
    email_address='person@pie.com',
    phone='333-333-3333',
    password='password'
)
session.add(cookiemon)
session.add(cakeeater)
session.add(pieperson)
session.commit()

# %% First order
o1 = Order()
o1.user = cookiemon
session.add(o1)

cc = session.query(Cookie).filter(Cookie.cookie_name == 'chocolate chip').one()
line1 = LineItem(cookie=cc, quantity=2, extended_cost=1.00)

pb = session.query(Cookie).filter(Cookie.cookie_name == 'peanut butter').one()
line2 = LineItem(quantity=12, extended_cost=3.00)
line2.cookie = pb
line2.order = o1

o1.line_items.append(line1)
o1.line_items.append(line2)
session.commit()

# %% Second order
o2 = Order()
o2.user = cakeeater

cc = session.query(Cookie).filter(Cookie.cookie_name == 'chocolate chip').one()
line1 = LineItem(cookie=cc, quantity=24, extended_cost=12.00)

oat = session.query(Cookie).filter(Cookie.cookie_name == 'oatmeal raisin').one()
line2 = LineItem(cookie=oat, quantity=6, extended_cost=6.00)

o2.line_items.append(line1)
o2.line_items.append(line2)
session.add(o2)
session.commit()
