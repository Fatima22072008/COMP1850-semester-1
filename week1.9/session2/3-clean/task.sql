.headers on
.mode column

-- add tasks below
-- sqlite3 database_file.db to open the database
-- .read sql_file.sql to run the queries

-- YOU SHOULD RUN ANY 'UPDATES' AS SELECTS FIRST - it's very easy to accidentally update more than you intended..

-- this updates the restaurants so that italian is spelt in the right format
UPDATE restaurants
SET cuisine = 'Italian'
WHERE cuisine = 'ITALIAN';

UPDATE restaurants
SET cuisine = 'Italian'
WHERE cuisine = 'italian';

-- here we can make every postcode captial, it applies to all postcodes in the table becuase we didnt use where
UPDATE restaurants
SET postcode = UPPER(postcode);

-- this deletes every row where an email ends with test making use of the LIKE operator
DELETE FROM customers
WHERE email LIKE '%@test.com';

-- deleting duplicates from the table restaurants
