from sqlalchemy import select
from sqlalchemy.sql import func

from src.part1.chapter2.limiting import cookies, connection

# How many cookies do we have
selection = select([func.sum(cookies.c.quantity)])
result_proxy = connection.execute(selection)
assert result_proxy.scalar() == 137

# Home many unique cookie flavors do we have
selection = select([func.count(cookies.c.cookie_name)])
result_proxy = connection.execute(selection)
record = result_proxy.first()
assert record.keys() == ['count_1']
assert record.count_1 == 4

# Label count column with human-readable value
selection = select([func.count(cookies.c.cookie_name).label('inventory_count')])
result_proxy = connection.execute(selection)
record = result_proxy.first()
assert record.keys() == ['inventory_count']
assert record.inventory_count == 4
