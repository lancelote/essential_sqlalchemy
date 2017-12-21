# from pprint import pprint

from sqlalchemy import insert

from src.part1.chapter1.in_memory_full_example import cookies, engine

ins = cookies.insert().values(
    cookie_name='chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
    cookie_sku='CC01',
    quantity='12',
    unit_cost='0.50'
)

# print(str(ins))
# INSERT INTO cookies
#   (cookie_name, cookie_recipe_url, cookie_sku, quantity, unit_cost)
# VALUES
#   (:cookie_name, :cookie_recipe_url, :cookie_sku, :quantity, :unit_cost)

# pprint(ins.compile().params)
# {'cookie_name': 'chocolate chip',
#  'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe.html',
#  'cookie_sku': 'CC01',
#  'quantity': '12',
#  'unit_cost': '0.50'}

connection = engine.connect()
result = connection.execute(ins)
assert result.inserted_primary_key == [1]

# Insert can also be called as a top-level function
ins2 = insert(cookies).values(
    cookie_name='chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
    cookie_sku='CC01',
    quantity='12',
    unit_cost='0.50'
)

# Provide values for insertion separately
ins3 = cookies.insert()
result3 = connection.execute(
    ins3,
    cookie_name='dark chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
    cookie_sku='CC02',
    quantity='1',
    unit_cost='0.75'
)
assert result3.inserted_primary_key == [2]

# Insert multiple values
inventory_list = [
    {
        'cookie_name': 'peanut butter',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
        'cookie_sku': 'PB01',
        'quantity': '24',
        'unit_cost': '0.25'
    },
    {
        'cookie_name': 'oatmeal raisin',
        'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
        'cookie_sku': 'EWW01',
        'quantity': '100',
        'unit_cost': '1.00'
    }
]
connection.execute(ins, *inventory_list)
