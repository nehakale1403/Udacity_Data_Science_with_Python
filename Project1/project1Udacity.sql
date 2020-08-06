
//1
SELECT
  f.title film_title,
  c.name film_category,
  COUNT(r.rental_date) rental_count
FROM film f
JOIN film_category fc
  ON fc.film_id = f.film_id
JOIN category c
  ON fc.category_id = c.category_id
JOIN inventory i
  ON i.film_id = f.film_id
JOIN rental r
  ON r.inventory_id = i.inventory_id
GROUP BY 1,
         2
ORDER BY 2, 1;

//2

SELECT
  *,
  NTILE(4) OVER (ORDER BY t1.rental_duration) AS standard_quartile
FROM (SELECT
  f.title,
  c.name,
  f.rental_duration
FROM category AS c
JOIN film_category AS fc
  ON fc.category_id = c.category_id
  AND c.name IN ('Animation', 'Children', 'Comedy', 'Classics', 'Comedy', 'Family', 'Music')
JOIN film AS f
  ON f.film_id = fc.film_id
ORDER BY 2, 1) t1;

//3 

SELECT
   DATE_PART('year', r1.rental_date) AS rental_year,
   DATE_PART('month', r1.rental_date) AS rental_month,
   (
      'Store ' || s1.store_id
   )
   AS store,
   COUNT(*) 
FROM
   store as s1 
   JOIN
      staff as s2 
      ON s1.store_id = s2.store_id 
   JOIN
      rental r1 
      ON s2.staff_id = r1.staff_id 
GROUP BY
   1,
   2,
   3 
ORDER BY
   2,
   1;

//4

WITH t1 AS 
(
   SELECT
(first_name || ' ' || last_name) AS name,
      c.customer_id,
      p.amount,
      p.payment_date 
   FROM
      customer AS c 
      JOIN
         payment AS p 
         ON c.customer_id = p.customer_id
)
,
t2 AS 
(
   SELECT
      t1.customer_id 
   FROM
      t1 
   GROUP BY
      1 
   ORDER BY
      SUM(t1.amount) DESC LIMIT 10
)
SELECT
   t1.name,
   DATE_PART('month', t1.payment_date) AS payment_month,
   DATE_PART('year', t1.payment_date) AS payment_year,
   COUNT (*),
   SUM(t1.amount) 
FROM
   t1 
   JOIN
      t2 
      ON t1.customer_id = t2.customer_id 
WHERE
   t1.payment_date BETWEEN '20070101' AND '20080101' 
GROUP BY
   1,
   2,
   3;


