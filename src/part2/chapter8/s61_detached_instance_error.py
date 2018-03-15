from sqlalchemy.orm.exc import DetachedInstanceError

from src.part2.chapter8.s58_db_setup import Cookie, LineItem, Order, User
from src.part2.chapter8.s60_multiple_results_found import session

cookiemon = User('cookiemon', 'mon@cookie.com', '111-111-1111', 'password')
session.add(cookiemon)
o1 = Order()
o1.user = cookiemon
session.add(o1)

cc = session.query(Cookie).filter(Cookie.cookie_name ==
                                  "Change chocolate chip").one()
line1 = LineItem(order=o1, cookie=cc, quantity=2, extended_cost=1.00)
session.add(line1)
session.commit()

# Trigger exception
order = session.query(Order).first()
session.expunge(order)  # Detach order from session

try:
    result = order.line_items
except DetachedInstanceError:
    pass
else:
    raise AssertionError('Expected to raise DetachedInstanceError')
