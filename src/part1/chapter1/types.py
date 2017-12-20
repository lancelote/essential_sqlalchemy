# Standard types are in all capital letters
from sqlalchemy.types import BOOLEAN

# Dialect specific type
from sqlalchemy.dialects.postgresql import JSON

print(BOOLEAN, JSON)
