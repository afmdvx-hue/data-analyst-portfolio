-- Supply chain KPI analysis (SQLite: data/portfolio.db)
-- Build: npm run db:build  |  Data: npm run fetch:supply-chain

-- 1) Supplier ranking — revenue vs quality risk
SELECT "Supplier name" AS supplier,
       COUNT(*) AS skus,
       ROUND(SUM("Revenue generated"), 2) AS total_revenue,
       ROUND(AVG("Lead time"), 1) AS avg_lead_days,
       ROUND(AVG("Defect rates"), 2) AS avg_defect_pct,
       ROUND(100.0 * AVG(CASE WHEN "Lead time" <= 20 THEN 1.0 ELSE 0 END), 1) AS on_time_pct
FROM supply_chain_skus
GROUP BY "Supplier name"
ORDER BY avg_defect_pct DESC, avg_lead_days DESC;

-- 2) Top 5 SKUs to inspect (defect rate)
SELECT SKU,
       "Product type" AS product_type,
       "Supplier name" AS supplier,
       ROUND("Defect rates", 2) AS defect_pct,
       "Lead time" AS lead_days
FROM supply_chain_skus
ORDER BY "Defect rates" DESC
LIMIT 5;

-- 3) Revenue by product line with margin proxy
SELECT "Product type",
       COUNT(*) AS skus,
       ROUND(SUM("Revenue generated"), 2) AS revenue,
       ROUND(SUM("Costs"), 2) AS costs,
       ROUND(100.0 * (SUM("Revenue generated") - SUM("Costs")) / SUM("Revenue generated"), 1) AS margin_pct
FROM supply_chain_skus
GROUP BY "Product type"
ORDER BY revenue DESC;

-- 4) Carrier performance (window: rank by cost within carrier volume)
SELECT "Shipping carriers" AS carrier,
       COUNT(*) AS orders,
       ROUND(AVG("Shipping times"), 1) AS avg_days,
       ROUND(AVG("Shipping costs"), 2) AS avg_cost
FROM supply_chain_skus
GROUP BY "Shipping carriers"
ORDER BY orders DESC;

-- 5) SKUs failing both lead-time and quality thresholds
SELECT SKU,
       "Supplier name",
       "Defect rates",
       "Lead time"
FROM supply_chain_skus
WHERE "Defect rates" >= 3.0
  AND "Lead time" > 20
ORDER BY "Defect rates" DESC;
