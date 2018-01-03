from sqlalchemy import and_, or_, select

from src.part1.chapter2.s19_operators import cookies, connection

# List of cookies with a cost of less than an amount and above certain quantity
selection = select([cookies]).where(
    and_(
        cookies.c.quantity > 23,
        cookies.c.unit_cost < 0.40
    )
)
result_proxy = connection.execute(selection)
record = result_proxy.first()
assert record.cookie_name == 'peanut butter'

# Cookie type between 10 and 50 in stock or name contains "chip"
selection = select([cookies]).where(
    or_(
        cookies.c.quantity.between(10, 50),
        cookies.c.cookie_name.contains('chip')
    )
)
result_proxy = connection.execute(selection)
records = result_proxy.fetchall()
cookie_names = [record.cookie_name for record in records]
assert cookie_names == ['chocolate chip', 'dark chocolate chip', 'peanut butter']
