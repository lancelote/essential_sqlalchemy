from sqlalchemy import CheckConstraint, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SomeDataClass(Base):
    __tablename__ = 'some_data_table'
    __table_args__ = (ForeignKeyConstraint(['id'], ['other_table.id']),
                      CheckConstraint('unit_cost >= 0.00', name='unit_cost_positive'))
