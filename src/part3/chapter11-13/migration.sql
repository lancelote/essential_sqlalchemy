-- Running upgrade d0e8bc40ad9e -> 1245487395c7

ALTER TABLE cookies RENAME TO new_cookies;

UPDATE alembic_version SET version_num='1245487395c7' WHERE alembic_version.version_num = 'd0e8bc40ad9e';

