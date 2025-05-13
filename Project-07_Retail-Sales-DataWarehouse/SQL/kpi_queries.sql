================================================================================

-- Total Revenue KPI
SELECT
  ROUND(SUM(total_amount), 2) AS total_revenue
FROM
  `retail-data-warehouse.retail_data.sales`;

================================================================================

--Top 5 Products by Revenue
SELECT
  p.product_name,
  ROUND(SUM(s.total_amount), 2) AS revenue
FROM
  `retail-data-warehouse.retail_data.sales` s
JOIN
  `retail-data-warehouse.retail_data.products` p
ON
  s.product_id = p.product_id
GROUP BY
  p.product_name
ORDER BY
  revenue DESC
LIMIT 5;


================================================================================

--Revenue by Store
SELECT
  st.store_name,
  ROUND(SUM(s.total_amount), 2) AS revenue
FROM
  `retail-data-warehouse.retail_data.sales` s
JOIN
  `retail-data-warehouse.retail_data.stores` st
ON
  s.store_id = st.store_id
GROUP BY
  st.store_name
ORDER BY
  revenue DESC;


================================================================================

--Daily Revenue Trend
SELECT
  d.date,
  ROUND(SUM(s.total_amount), 2) AS daily_revenue
FROM
  `retail-data-warehouse.retail_data.sales` s
JOIN
  `retail-data-warehouse.retail_data.date_dim` d
ON
  DATE(s.sale_date) = d.date
GROUP BY
  d.date
ORDER BY
  d.date;


================================================================================

