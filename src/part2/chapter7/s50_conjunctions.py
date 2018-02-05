from sqlalchemy import or_

from src.part2.chapter7.s49_operators import Cookie, session

# List of cookies with a cost of less than an amount and above a certain quantity
query = session.query(Cookie).filter(
    Cookie.quantity > 23,
    Cookie.unit_cost < 0.40
)
assert [result.cookie_name for result in query] == ['peanut butter']

# Cookie types that we have between 10 and 50 of in stock or where the name contains "chip"
query = session.query(Cookie).filter(
    or_(
        Cookie.quantity.between(10, 50),
        Cookie.cookie_name.contains('chip')
    )
)
assert [result.cookie_name for result in query] == ['chocolate chip', 'dark chocolate chip', 'peanut butter']
