# goit-rdb-hw-07
1)
SELECT 
	id, 
  	date, 
	 YEAR(date) as year,
  	MONTH(date) as month,
  	DAY(date) as day
FROM orders;

2)
SELECT
	id, 
    	date, 
    	DATE_ADD(date, INTERVAL 1 DAY) as next_day
FROM orders;

3)
SELECT 
	id, 
    	date, 
    	UNIX_TIMESTAMP(date) as timestamp_date
FROM orders;

4)
SELECT COUNT(*) AS count_date_btw
FROM orders
WHERE date BETWEEN '1996-07-10 00:00:00' AND '1996-10-08 00:00:00';

5)
SELECT 
	id,
    	date,
    	JSON_OBJECT('id', id, 'date', date) as json_object
FROM orders;
