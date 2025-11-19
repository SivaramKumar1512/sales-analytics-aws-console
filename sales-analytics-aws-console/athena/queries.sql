-- Athena queries for sales_clean_sivam01
-- Adjust table name if your Glue crawler created a different name.

-- Preview
SELECT * FROM "sales_db"."sales_clean_sivam01" LIMIT 10;

-- Describe schema
DESCRIBE "sales_db"."sales_clean_sivam01";

-- Count rows
SELECT count(*) AS total_rows FROM "sales_db"."sales_clean_sivam01";

-- Cast and check numeric fields
SELECT product, CAST(quantity AS INTEGER) AS quantity_int, CAST(price AS DOUBLE) AS price_num
FROM "sales_db"."sales_clean_sivam01" LIMIT 10;

-- Total revenue per product
SELECT product, SUM(CAST(quantity AS INTEGER) * CAST(price AS DOUBLE)) AS total_revenue,
       SUM(CAST(quantity AS INTEGER)) AS total_qty
FROM "sales_db"."sales_clean_sivam01"
GROUP BY product
ORDER BY total_revenue DESC;

-- Optional view (create in Athena for QuickSight / reporting)
CREATE OR REPLACE VIEW sales_db.view_product_revenue AS
SELECT product,
       SUM(CAST(quantity AS INTEGER) * CAST(price AS DOUBLE)) AS total_revenue,
       SUM(CAST(quantity AS INTEGER)) AS total_qty
FROM "sales_db"."sales_clean_sivam01"
GROUP BY product;
