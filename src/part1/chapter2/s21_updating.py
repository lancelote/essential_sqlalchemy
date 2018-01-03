from sqlalchemy import update, select

from src.part1.chapter2.s20_conjunctions import cookies, connection

selection = update(cookies).where(cookies.c.cookie_name == 'chocolate chip')
selection = selection.values(quantity=(cookies.c.quantity + 120))
result_proxy = connection.execute(selection)
assert result_proxy.rowcount == 1

selection = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')
result_proxy = connection.execute(selection).first()
# for key in result_proxy.keys():
#     print('{:>20}: {}'.format(key, result_proxy[key]))
#
#            cookie_id: 1
#          cookie_name: chocolate chip
#    cookie_recipe_url: http://some.aweso.me/cookie/recipe.html
#           cookie_sku: CC01
#             quantity: 132
#            unit_cost: 0.50
