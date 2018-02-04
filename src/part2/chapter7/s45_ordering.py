from sqlalchemy import desc

from src.part2.chapter7.s44_controlling_query_columns import Cookie, session

results = []
for cookie in session.query(Cookie).order_by(Cookie.quantity):
    results.append('{:3} - {}'.format(cookie.quantity, cookie.cookie_name))
assert results == [
    '  1 - dark chocolate chip',
    '  1 - molasses',
    ' 12 - chocolate chip',
    ' 24 - peanut butter',
    '100 - oatmeal raisin',
]

# Descending order
first = session.query(Cookie).order_by(desc(Cookie.quantity)).first()
assert '{:3} - {}'.format(first.quantity, first.cookie_name) == '100 - oatmeal raisin'
