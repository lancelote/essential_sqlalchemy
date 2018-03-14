from src.part2.chapter8.s58_db_setup import Cookie, Order, User
from src.part2.chapter8.s60_multiple_results_found import session

cookiemon = User('cookiemon', 'mon@cookie.com', '111-111-1111', 'password')
session.add(cookiemon)
o1 = Order()
o1.user = cookiemon
session.add(o1)

cc = session.query(Cookie).filter(Cookie.cookie_name ==
                                  "Change chocolate chip")
print(cc)
# ToDo: fix error
