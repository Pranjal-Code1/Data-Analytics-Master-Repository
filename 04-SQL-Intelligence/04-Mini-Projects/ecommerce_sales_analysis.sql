-- ====================================================================
-- Author: Pranjal
-- Module: 04-SQL-Intelligence / 04-Mini-Projects
-- Project: E-Commerce Performance & Customer Segmentation Analysis
-- Description: End-to-end analytical queries answering core business questions
--              regarding top-selling categories, repeat buyers, and revenue trends.
-- ====================================================================

-- BUSINESS OBJECTIVE 1: Identify the top 3 highest-grossing product categories
SELECT 
    p.category,
    SUM(o.quantity) AS total_units_sold,
    SUM(o.total_price) AS total_revenue
FROM 
    products p
JOIN 
    order_items o ON p.product_id = o.product_id
GROUP BY 
    p.category
ORDER BY 
    total_revenue DESC
LIMIT 3;

-- BUSINESS OBJECTIVE 2: Segment customers based on lifetime spending (High, Medium, Low)
WITH CustomerSpending AS (
    SELECT 
        customer_id,
        SUM(total_price) AS lifetime_spend
    FROM 
        orders
    GROUP BY 
        customer_id
)
SELECT 
    customer_id,
    lifetime_spend,
    CASE 
        WHEN lifetime_spend > 10000 THEN 'VIP High-Value'
        WHEN lifetime_spend BETWEEN 5000 AND 10000 THEN 'Medium-Tier'
        ELSE 'Standard'
    END AS customer_segment
FROM 
    CustomerSpending
ORDER BY 
    lifetime_spend DESC;