from src.part2.chapter7.s43_querying_data import Cookie, session

assert session.query(Cookie.cookie_name, Cookie.quantity).first() == ('chocolate chip', 12)
