from sqlalchemy import inspect
from sqlalchemy.orm.attributes import History

from src.part2.chapter8.s58_db_setup import Cookie, session

cc_cookie = Cookie(
    'chocolate chip',
    'http://some.aweso.me/cookie/recipe.html',
    'CC01', 12, 0.50
)

insp = inspect(cc_cookie)
assert insp.transient

session.add(cc_cookie)
assert insp.pending

session.commit()
assert insp.persistent

session.expunge(cc_cookie)
assert insp.detached

session.add(cc_cookie)
cc_cookie.cookie_name = 'Change chocolate chip'
assert insp.modified

for attr, attr_state in insp.attrs.items():
    if attr_state.history.has_changes():
        assert attr == 'cookie_name'
        assert attr_state.value == 'Change chocolate chip'
        assert attr_state.history == History(added=['Change chocolate chip'], unchanged=(), deleted=())
