-- The cities of California
-- SELECT query
SELECT id, name FROM cities
 WHERE state_id = 
            (SELECT id 
               FROM states 
              WHERE name 
               LIKE "California")
 ORDER BY id;
