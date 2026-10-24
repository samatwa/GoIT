# goit-rdb-hw-03

1)
SELECT * 
FROM mydb.products;

SELECT name, phone
FROM mydb.shippers;

2)
SELECT
	ROUND(AVG(price), 2) AS average_price,
	MAX(price) AS max_price,
	MIN(price) AS min_price
FROM mydb.products;

3)
SELECT DISTINCT category_id, price
FROM mydb.products
ORDER BY 2 DESC
LIMIT 10;

4)
SELECT COUNT(*) AS product_count
FROM mydb.products
WHERE price BETWEEN 20 AND 100;

5)
SELECT 
	supplier_id,
	COUNT(*) AS product_count,
    ROUND(AVG(price)) AS average_price
FROM mydb.products
GROUP BY supplier_id;

 
