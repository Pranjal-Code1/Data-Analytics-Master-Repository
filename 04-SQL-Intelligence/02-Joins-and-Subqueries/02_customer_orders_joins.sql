-- ====================================================================
-- Author: Pranjal
-- Module: 04-SQL-Intelligence / 02-Joins-and-Subqueries
-- Description: Practicing multi-table joins (INNER, LEFT) and aggregations
--              to analyze customer purchasing behavior.
-- ====================================================================

-- 1. INNER JOIN: Finding total revenue generated per customer
SELECT 
    c.customer_id,
    c.customer_name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.order_amount) AS total_spent
FROM 
    customers c
INNER JOIN 
    orders o ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_id, 
    c.customer_name
ORDER BY 
    total_spent DESC;

-- 2. LEFT JOIN: Identifying customers who have registered but never placed an order
SELECT 
    c.customer_id,
    c.customer_name,
    c.signup_date
FROM 
    customers c
LEFT JOIN 
    orders o ON c.customer_id = o.customer_id
WHERE 
    o.order_id IS NULL;