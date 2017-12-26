from sqlalchemy import select, cast, Numeric

from src.part1.chapter2.filtering import cookies, connection

# String concatenation
selection = select([cookies.c.cookie_name, 'SKU-' + cookies.c.cookie_sku])
result_proxy = connection.execute(selection)
records = result_proxy.fetchall()
assert len(records) == 4

# print(records)
#
# [('chocolate chip', 'SKU-CC01'),
#  ('dark chocolate chip', 'SKU-CC02'),
#  ('peanut butter', 'SKU-PB01'),
#  ('oatmeal raisin', 'SKU-EWW01')]

# Type casting - inventory value by cookie
selection = select([cookies.c.cookie_name, cast((cookies.c.quantity * cookies.c.unit_cost),
                                                Numeric(12, 2)).label('inv_cost')])
result_proxy = connection.execute(selection)
records = result_proxy.fetchall()

# for record in records:
#     print('{} - {}'.format(record.cookie_name, record.inv_cost))
#
# chocolate chip - 6.00
# dark chocolate chip - 0.75
# peanut butter - 6.00
# oatmeal raisin - 100.00
