.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- bronze
-- SELECT * FROM drivers;

--SELECT name, price FROM menu_items
-- WHERE restaurant_id = 3;

--SELECT name FROM restaurants
--WHERE cuisine = 'Indian';

-- SELECT COUNT(*) FROM customers;

-- silver

--SELECT name FROM menu_items
--WHERE is_vegetarian = 1 AND price < 8.00
--ORDER by price DESC;

--SELECT name FROM restaurants
--WHERE hygiene_rating < 4
--ORDER by hygiene_rating ASC;

--SELECT name FROM restaurants
--WHERE postcode LIKE 'LS6%' 
--ORDER BY hygiene_rating ASC;

--SELECT email FROM customers
--WHERE email LIKE '%leeds.ac.uk'
--ORDER by joined_date DESC;

--SELECT name FROM menu_items
--WHERE restaurant_id = 4 AND is_vegetarian = 1;
--SELECT MAX(price) FROM menu_items
--WHERE restaurant_id = 4;

-- GOLD

--SELECT name, price FROM menu_items
--WHERE is_vegetarian = 1
--ORDER BY price LIMIT 5;

--SELECT MIN(price), name FROM menu_items;
--ORDER BY price LIMIT 1;

