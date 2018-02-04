from src.part2.chapter7.s45_ordering import Cookie, session

query = session.query(Cookie).order_by(Cookie.quantity)[:2]
assert [result.cookie_name for result in query] == ['dark chocolate chip', 'molasses']

# Limit method
query = session.query(Cookie).order_by(Cookie.quantity).limit(2)
assert [result.cookie_name for result in query] == ['dark chocolate chip', 'molasses']
