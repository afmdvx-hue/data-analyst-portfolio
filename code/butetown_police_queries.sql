-- Butetown / Cardiff crime analysis (SQLite: data/portfolio.db)
-- Build tables: npm run db:build  (after npm run fetch:police)

-- 1) Total incidents by area (36 months of API data)
SELECT area,
       SUM(crime_count) AS total_incidents
FROM crime_monthly
GROUP BY area
ORDER BY total_incidents DESC;

-- 2) Butetown monthly trend (last 12 months)
SELECT month,
       crime_count
FROM crime_monthly
WHERE area = 'Butetown'
ORDER BY month DESC
LIMIT 12;

-- 3) Butetown vs Cardiff Bay — same month comparison
SELECT b.month,
       b.crime_count AS butetown,
       c.crime_count AS cardiff_bay,
       ROUND(100.0 * b.crime_count / NULLIF(c.crime_count, 0), 1) AS butetown_vs_bay_pct
FROM crime_monthly b
JOIN crime_monthly c ON b.month = c.month AND c.area = 'Cardiff Bay'
WHERE b.area = 'Butetown'
ORDER BY b.month DESC
LIMIT 12;

-- 4) Top crime categories in Butetown
SELECT category,
       crime_count
FROM crime_categories
WHERE area = 'Butetown'
ORDER BY crime_count DESC
LIMIT 8;

-- 5) Year-over-year Butetown (from month strings YYYY-MM)
SELECT SUBSTR(month, 1, 4) AS year,
       SUM(crime_count) AS incidents
FROM crime_monthly
WHERE area = 'Butetown'
GROUP BY year
ORDER BY year;
