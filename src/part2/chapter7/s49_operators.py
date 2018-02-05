from sqlalchemy import Numeric, cast

from src.part2.chapter7.s48_filtering import Cookie, session

results = session.query(Cookie.cookie_name, 'SKU-' + Cookie.cookie_sku).all()
assert results == [
    ('chocolate chip', 'SKU-CC01'),
    ('dark chocolate chip', 'SKU-CC02'),
    ('molasses', 'SKU-MOL01'),
    ('peanut butter', 'SKU-PB01'),
    ('oatmeal raisin', 'SKU-EWW01')
]

query = session.query(
    Cookie.cookie_name, cast((Cookie.quantity * Cookie.unit_cost), Numeric(12, 2)).label('inv_cost'))
results = []
for result in query:
    results.append('{} - {}'.format(result.cookie_name, result.inv_cost))
assert results == [
    'chocolate chip - 6.00',
    'dark chocolate chip - 0.75',
    'molasses - 0.80',
    'peanut butter - 6.00',
    'oatmeal raisin - 100.00',
]
