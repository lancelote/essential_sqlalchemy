from sqlalchemy import Table, Column, Integer, ForeignKey, select, and_, String

from src.part1.chapter1.s10_in_memory_full_example import metadata

employee_table = Table(
    'employee', metadata,
    Column('id', Integer, primary_key=True),
    Column('manager_id', None, ForeignKey('employee.id')),
    Column('name', String(255)),
)

# Select all employees managed by an employee named Fred
manager = employee_table.alias('manager')
stmt = select([employee_table.c.name], and_(
    employee_table.c.manager_id == manager.c.id, manager.c.name == 'Fred'))
assert str(stmt).startswith('SELECT employee.name')

# print(stmt)
#
# SELECT employee.name
# FROM employee, employee AS manager
# WHERE employee.manager_id = manager.id AND manager.name = :name_1

# Automatic alias selection
manager = employee_table.alias()
stmt = select([employee_table.c.name], and_(
    employee_table.c.manager_id == manager.c.id, manager.c.name == 'Fred'))
assert 'employee_1' in str(stmt)

# print(stmt)
#
# SELECT employee.name
# FROM employee, employee AS employee_1
# WHERE employee.manager_id = employee_1.id AND employee_1.name = :name_1
