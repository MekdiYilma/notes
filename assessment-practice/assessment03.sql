SELECT  * 
FROM address a2
LIMIT 5;


SELECT city, postal_code 
FROM address a2 
JOIN city c2 
ON a2.city_id = c2.city_id 
WHERE city LIKE 'Bu%';

SELECT 
	customer_id ,
	count(*) AS purchase
FROM payment p2 
GROUP BY customer_id 
ORDER BY 2 DESC
LIMIT 1;


SELECT 
	customer_id ,
	count(*) AS purchase,
	sum(amount) 
FROM payment p2 
GROUP BY customer_id 
ORDER BY 3
LIMIT 1;


SELECT * 
FROM film f 
LIMIT 5;


SELECT title 
FROM film f 
WHERE rental_rate  =  0.99 OR length <60;


-- REDOING THE ASSESSMENT
SELECT DISTINCT (postal_code)
FROM customer c 
JOIN address a
USING (address_id)
WHERE district LIKE 'Buenos%';

SELECT DISTINCT (postal_code)
FROM 
address a 
WHERE district LIKE 'Buenos%';


SELECT c.customer_id, count(amount)
FROM customer c 
JOIN payment p 
USING (customer_id)
GROUP BY c.customer_id 
ORDER BY 2 DESC
LIMIT 1;

SELECT * 
FROM customer c 
LIMIT 5;

SELECT customer_id , count(*)
FROM payment p 
GROUP BY customer_id 
ORDER BY 2 DESC
LIMIT 1;


SELECT customer_id , sum(amount)
FROM payment p 
GROUP BY customer_id 
ORDER BY 2 ASC
LIMIT 1;


SELECT *
FROM film f 
LIMIT 5;

SELECT title 
FROM film f 
WHERE rental_rate = 0.99
OR length <50






