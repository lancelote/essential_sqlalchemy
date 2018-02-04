from sqlalchemy import func

from src.part2.chapter7.s46_limiting import Cookie, session

# Total number of cookies
inventory_count = session.query(func.sum(Cookie.quantity)).scalar()
assert inventory_count == 138

# Total number of different cookie types
record_count = session.query(func.count(Cookie.cookie_name)).first()
assert record_count == (5,)

# More readable result
record_count = session.query(func.count(Cookie.cookie_name).label('inventory_count')).first()
assert record_count.keys() == ['inventory_count']
assert record_count.inventory_count == 5
