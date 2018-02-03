from src.part2.chapter7.s41_session import Cookie, session

cc_cookie = Cookie(
    cookie_name='chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
    cookie_sku='CC01',
    quantity=12,
    unit_cost=0.50
)
session.add(cc_cookie)
session.commit()

assert cc_cookie.cookie_id == 1

dcc = Cookie(
    cookie_name='dark chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
    cookie_sku='CC02',
    quantity=1,
    unit_cost=0.75
)
mol = Cookie(
    cookie_name='molasses',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe_molasses.html',
    cookie_sku='MOL01',
    quantity=1,
    unit_cost=0.80
)
session.add(dcc)
session.add(mol)
session.flush()  # dcc and mol are still connected and can be used
assert dcc.cookie_id == 2
assert mol.cookie_id == 3

# Do not associate the records with the session
c1 = Cookie(
    cookie_name='peanut butter',
    cookie_recipe_url='http://some.aweso.me/cookie/peanut.html',
    cookie_sku='PB01',
    quantity=24,
    unit_cost=0.25
)
c2 = Cookie(
    cookie_name='oatmeal raisin',
    cookie_recipe_url='http://some.okay.me/cookie/raisin.html',
    cookie_sku='EWW01',
    quantity=100,
    unit_cost=1.00
)
session.bulk_save_objects([c1, c2])
session.commit()
assert c1.cookie_id is None
