-- lists all records of the table second_table
-- Don’t list rows without a name value
SELECT score, name from second_table
WHERE name is not NULL;
