-- ====================================================================
-- Author: Pranjal
-- Module: 04-SQL-Intelligence / 03-Advanced-SQL
-- Description: Practicing advanced SQL concepts including CTEs, 
--              ROW_NUMBER(), RANK(), and running totals.
-- ====================================================================

-- 1. Using a CTE (Common Table Expression) to pre-aggregate data
WITH MonthlySales AS (
    SELECT 
        DATE_TRUNC('month', order_date) AS order_month,
        SUM(order_amount) AS monthly_revenue
    FROM 
        orders
    GROUP BY 
        1
)
SELECT 
    order_month,
    monthly_revenue,
    -- 2. Window Function: Calculating running total revenue over time
    SUM(monthly_revenue) OVER (ORDER BY order_month) AS cumulative_revenue
FROM 
    MonthlySales;

-- 3. Ranking employees or products using RANK() vs ROW_NUMBER()
SELECT 
    department,
    employee_name,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as emp_row_num,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as emp_rank
FROM 
    employees;