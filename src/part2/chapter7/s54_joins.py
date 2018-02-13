from decimal import Decimal

from sqlalchemy import Column, ForeignKey, Integer, String, func
from sqlalchemy.orm import backref, relationship

from src.part2.chapter7.s41_session import Base, engine
from src.part2.chapter7.s53_load_data import Cookie, LineItem, Order, User, session

# %% Basic join query
query = session.query(
    Order.order_id,
    User.username,
    User.phone,
    Cookie.cookie_name,
    LineItem.quantity,
    LineItem.extended_cost
)
query = query.join(User).join(LineItem).join(Cookie)
results = query.filter(User.username == 'cookiemon').all()

assert results == [
    (1, 'cookiemon', '111-111-1111', 'peanut butter', 12, Decimal('3.00')),
    (1, 'cookiemon', '111-111-1111', 'chocolate chip', 2, Decimal('1.00'))
]

# %% Outer join
query = session.query(User.username, func.count(Order.order_id))
query = query.outerjoin(Order).group_by(User.username)
assert query.all() == [
    ('cakeeater', 1),
    ('cookiemon', 1),
    ('pieperson', 0)
]


# %% Many-to-one relationship and self reference
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer(), primary_key=True)
    manager_id = Column(Integer(), ForeignKey('employees.id'))
    name = Column(String(255), nullable=False)
    manager = relationship('Employee', backref=backref('reports'), remote_side=[id])


Base.metadata.create_all(engine)

marsha = Employee(name='Marsha')
fred = Employee(name='Fred')

marsha.reports.append(fred)

session.add(marsha)
session.commit()

assert list(marsha.reports)[0].name == 'Fred'
