-- lists the number of records with the same score in the table

SELECT COUNT(score), score
FROM second_table
GROUP BY score DESC;