from sqlalchemy import delete, select

from src.part1.chapter2.s21_updating import cookies, connection

selection = delete(cookies).where(cookies.c.cookie_name == 'dark chocolate chip')
result_proxy = connection.execute(selection)
assert result_proxy.rowcount == 1

selection = select([cookies]).where(cookies.c.cookie_name == 'dark chocolate chip')
result_proxy = connection.execute(selection).fetchall()
assert len(result_proxy) == 0  # Data was removed
