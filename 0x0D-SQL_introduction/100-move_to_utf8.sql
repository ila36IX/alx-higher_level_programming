-- converts hbtn_0c_0 database to UTF8
-- Specifying the database characterset
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- SELECT DATABASE
USE hbtn_0c_0;

-- Specifying the Table characterset
ALTER TABLE first_table
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Specifying the Column characterset
ALTER TABLE first_table MODIFY
name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
