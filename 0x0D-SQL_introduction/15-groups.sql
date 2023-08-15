-- Task 15
-- list ordered data
SELECT `score`, COUNT(*) AS `number` FROM `second_table`
GROUP BY `score` ORDER BY `score` DESC;
