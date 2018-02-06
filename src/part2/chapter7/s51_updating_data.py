from src.part2.chapter7.s50_conjunctions import Cookie, session

# %% Bake new cookies
query = session.query(Cookie)
cc_cookie = query.filter(Cookie.cookie_name == 'chocolate chip').first()
cc_cookie.quantity = cc_cookie.quantity + 120  # New cookies were made
session.commit()
assert cc_cookie.quantity == 132

# %% Update data in place
query = session.query(Cookie)
query = query.filter(Cookie.cookie_name == 'chocolate chip')
query.update({Cookie.quantity: Cookie.quantity - 20})
cc_cookie = query.first()
assert cc_cookie.quantity == 112
