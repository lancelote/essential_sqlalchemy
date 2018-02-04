from src.part2.chapter7.s42_inserting import Cookie, session

cookies = session.query(Cookie).all()
assert len(cookies) == 5

# Query as an iterable
for cookie in session.query(Cookie):
    assert isinstance(cookie, Cookie)
