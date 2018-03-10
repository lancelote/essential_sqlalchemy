from sqlalchemy.orm.exc import MultipleResultsFound

from src.part2.chapter8.s59_session_states import Cookie, session

dcc = Cookie(
    'dark chocolate chip',
    'http://some.aweso.me/cookie/recipe_dark.html',
    sku='CC02',
    quantity=1,
    unit_cost=0.75
)
session.add(dcc)
session.commit()

try:
    results = session.query(Cookie).one()
except MultipleResultsFound:
    pass
else:
    raise AssertionError('Expected to raise MultipleResultsFound')
