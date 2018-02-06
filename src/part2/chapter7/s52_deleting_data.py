from src.part2.chapter7.s51_updating_data import Cookie, session

# %% Delete data

query = session.query(Cookie)
query = query.filter(Cookie.cookie_name == 'dark chocolate chip')
dcc_cookie = query.one()
session.delete(dcc_cookie)
session.commit()
dcc_cookie = query.first()
assert dcc_cookie is None

# %% Delete data in place
query = session.query(Cookie)
query = query.filter(Cookie.cookie_name == 'molasses')
query.delete()
mol_cookie = query.first()
assert mol_cookie is None
