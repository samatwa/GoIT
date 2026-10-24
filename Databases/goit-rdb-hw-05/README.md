# goit-rdb-hw-05
1)
 SELECT 
	order_details.*,
	(SELECT customer_id 
	FROM orders 
    WHERE order_details.order_id = orders.id) AS customer_id
FROM order_details;

2)
SELECT *
FROM order_details
WHERE order_id IN (
	SELECT order_id
    	FROM orders
    	WHERE shipper_id = 3);
  
3)
SELECT 
	order_id, 
    	AVG(quantity) AS avg_q
FROM (
	SELECT *
    	FROM order_details
   	WHERE quantity > 10
    ) AS t
GROUP BY order_id;

4)
WITH temp AS (
	SELECT *
    	FROM order_details
   	 WHERE quantity > 10
)
SELECT 
	order_id, 
    	ROUND(AVG(quantity)) AS avg_q
FROM temp
GROUP BY order_id;

5)
DROP FUNCTION IF EXISTS Test;

DELIMITER //
CREATE FUNCTION  Test(num_1 FLOAT, num_2 FLOAT)
RETURNS FLOAT
DETERMINISTIC
NO SQL
BEGIN
	DECLARE result FLOAT;
    	IF num_2 = 0 THEN
		RETURN NULL;
	ELSE
		SET result = num_1 / num_2;
	END IF;
    	RETURN result;
END //

DELIMITER ;

SELECT Test(10.5, 3.2);

SELECT 
	order_id,
    	quantity,
    	Test(CAST(quantity AS FLOAT), 2.3) AS div_q
FROM order_details;

SELECT Test(10.5, 3.2);
