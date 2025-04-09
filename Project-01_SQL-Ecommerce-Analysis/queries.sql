/*
Total Revenue (Quantity × UnitPrice)
*/

SELECT ROUND(SUM(Quantity * UnitPrice), 2) AS total_revenue
FROM ecommerce_data;



/*
Top 10 Countries by Revenue
*/
SELECT Country, ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
FROM ecommerce_data
GROUP BY Country
ORDER BY revenue DESC
LIMIT 10;


/*
Top 10 Products by Revenue
*/
SELECT Description, ROUND(SUM(Quantity * UnitPrice), 2) AS revenue
FROM ecommerce_data
GROUP BY Description
ORDER BY revenue DESC
LIMIT 10;


/*
Monthly Revenue Trend
*/
SELECT DATE_TRUNC('month', InvoiceDate) AS month,
       ROUND(SUM(Quantity * UnitPrice), 2) AS monthly_revenue
FROM ecommerce_data
GROUP BY month
ORDER BY month;


/*
Number of Refunds (Negative Quantities)
*/
SELECT COUNT(*) AS refund_count
FROM ecommerce_data
WHERE Quantity < 0;


