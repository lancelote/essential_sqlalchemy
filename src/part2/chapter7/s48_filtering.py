from src.part2.chapter7.s47_built_in_sql_functions import Cookie, session

record = session.query(Cookie).filter(Cookie.cookie_name == 'chocolate chip').first()
assert record.cookie_name == 'chocolate chip'

record = session.query(Cookie).filter_by(cookie_name='chocolate chip').first()
assert record.cookie_name == 'chocolate chip'

# Find all the cookie names that contain the word "chocolate"
query = session.query(Cookie).filter(Cookie.cookie_name.like('%chocolate%'))
assert [record.cookie_name for record in query] == ['chocolate chip', 'dark chocolate chip']
