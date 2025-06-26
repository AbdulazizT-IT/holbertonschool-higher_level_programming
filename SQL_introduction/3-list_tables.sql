-- list of all tables of the database

SELECT Tables_in_hbtn_test_db_0
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = DATABASE();
