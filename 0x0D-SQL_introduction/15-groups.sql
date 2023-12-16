-- the number of records with the same score 
-- sorted by the number of records (descending)
SELECT score, count(score) as number
FROM second_table
GROUP BY SCORE
ORDER BY SCORE DESC;
