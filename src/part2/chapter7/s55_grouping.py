from sqlalchemy import func

from src.part2.chapter7.s54_joins import Order, User, session

query = session.query(User.username, func.count(Order.order_id))
query = query.outerjoin(Order).group_by(User.username)

assert list(query) == [('cakeeater', 1), ('cookiemon', 1), ('pieperson', 0)]
