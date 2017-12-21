# from pprint import pprint

from sqlalchemy.sql import select

from src.part1.chapter2.inserting import cookies, connection

selection = select([cookies])

print(str(selection))
# SELECT
#   cookies.cookie_id, cookies.cookie_name, cookies.cookie_recipe_url, cookies.cookie_sku, cookies.quantity,
#   cookies.unit_cost
# FROM cookies

result_proxy = connection.execute(selection)
result = result_proxy.fetchall()

# pprint(result)
# [(1, 'chocolate chip', 'http://some.aweso.me/cookie/recipe.html', 'CC01', 12, Decimal('0.50')),
#  (2, 'dark chocolate chip', 'http://some.aweso.me/cookie/recipe_dark.html', 'CC02', 1, Decimal('0.75')),
#  (3, 'peanut butter', 'http://some.aweso.me/cookie/peanut.html', 'PB01', 24, Decimal('0.25')),
#  (4, 'oatmeal raisin', 'http://some.okay.me/cookie/raisin.html', 'EWW01', 100, Decimal('1.00'))]

# Traditional declarative style
selection = cookies.select()
result_proxy = connection.execute(selection)
results = result_proxy.fetchall()
