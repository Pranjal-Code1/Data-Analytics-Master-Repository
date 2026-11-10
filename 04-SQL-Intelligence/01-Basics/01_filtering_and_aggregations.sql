-- ====================================================================
-- Author: Pranjal
-- Module: 04-SQL-Intelligence / 01-Basics
-- Description: Practicing foundational SQL concepts including SELECT, 
--              WHERE clauses, sorting, and aggregate functions.
-- ====================================================================

-- 1. Basic retrieval and filtering
SELECT 
    customer_id, 
    customer_name, 
    city, 
    signup_date
FROM 
    customers
WHERE 
    city = 'Delhi'
    AND signup_date >= '2025-01-01'
ORDER BY 
    signup_date DESC;

-- 2. Aggregation with GROUP BY
SELECT 
    department,
    COUNT(employee_id) AS total_employees,
    ROUND(AVG(salary), 2) AS average_salary
FROM 
    employees
GROUP BY 
    department
HAVING 
    COUNT(employee_id) > 2;