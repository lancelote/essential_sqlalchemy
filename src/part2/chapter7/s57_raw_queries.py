from sqlalchemy import text

from src.part2.chapter7.s56_chaining import User, session

query = session.query(User).filter(text("username='cookiemon'"))
assert len(query.all()) == 1
# [
#     User(
#         username='cookiemon',
#         email_address='mon@cookie.com',
#         phone='111-111-1111',
#         password='password'
#     )
# ]
