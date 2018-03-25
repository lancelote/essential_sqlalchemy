from sqlalchemy import create_engine, Column, Integer, String, Numeric, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()


class Cookie(Base):
    __tablename__ = 'cookies'

    cookie_id = Column(Integer(), primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))

    @hybrid_property
    def inventory_value(self):
        return self.unit_cost * self.quantity

    @hybrid_method
    def bake_more(self, min_quantity):
        return self.quantity < min_quantity

    def __repr__(self):
        return "Cookie(cookie_name='{self.cookie_name}', " \
               "cookie_recipe_url='{self.cookie_recipe_url}', " \
               "cookie_sku='{self.cookie_sku}', " \
               "quantity={self.quantity}, " \
               "unit_cost={self.unit_cost})".format(self=self)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

assert str(Cookie.inventory_value < 10.00) == 'cookies.unit_cost * cookies.quantity < :param_1'
assert str(Cookie.bake_more(12)) == 'cookies.quantity < :quantity_1'

# Add some data
session = Session()
cc_cookie = Cookie(
    cookie_name='chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
    cookie_sku='CC01',
    quantity=12,
    unit_cost=0.50
)
dcc = Cookie(
    cookie_name='dark chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
    cookie_sku='CC02',
    quantity=1,
    unit_cost=0.75
)
mol = Cookie(
    cookie_name='molasses',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe_molasses.html',
    cookie_sku='MOL01',
    quantity=1,
    unit_cost=0.80
)
session.add(cc_cookie)
session.add(dcc)
session.add(mol)
session.flush()

assert dcc.inventory_value == 0.75
assert dcc.bake_more

cookies = []
for cookie in session.query(Cookie).order_by(desc(Cookie.inventory_value)):
    cookies.append((cookie.cookie_name, cookie.inventory_value))

assert cookies == [
    ('chocolate chip', 6.0),
    ('molasses', 0.8),
    ('dark chocolate chip', 0.75)
]

cookies = []
for cookie in session.query(Cookie).filter(Cookie.bake_more(12)):
    cookies.append((cookie.cookie_name, cookie.quantity))

assert cookies == [
    ('dark chocolate chip', 1),
    ('molasses', 1)
]
