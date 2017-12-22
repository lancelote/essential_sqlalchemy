from src.part1.chapter2.querying import results, cookies, selection, connection

first_row = results[0]

# print(first_row)
# (1, 'chocolate chip', 'http://some.aweso.me/cookie/recipe.html', 'CC01', 12, Decimal('0.50'))

assert first_row[1] == 'chocolate chip'  # access column by index
assert first_row.cookie_name == 'chocolate chip'  # access column by name
assert first_row[cookies.c.cookie_name] == 'chocolate chip'  # access column by Column object

names = []
result_proxy = connection.execute(selection)  # Reusing previous selection

for record in result_proxy:
    names.append(record.cookie_name)

assert names == ['chocolate chip', 'dark chocolate chip', 'peanut butter', 'oatmeal raisin']
