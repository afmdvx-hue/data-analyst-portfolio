---
title: Butetown Community Impact Analysis
slug: butetown-community-impact
description: Data-driven report on crime, deprivation, and how Butetown's community sport clubs fill gaps left by structural failures in employment, education, and public safety.
date: "2026-06-01"
featured: true
hero: true
executiveSummary: /projects/butetown-community-impact/executive-summary.pdf
tags: ["Community Analytics", "Python", "SQL", "Visualisation", "Cardiff", "Social Impact"]
tools: ["Python", "Pandas", "SQL", "SQLite", "Matplotlib", "data.police.uk API", "Leaflet", "GeoJSON"]
metrics:
  - label: API months
    value: "36"
  - label: Butetown total
    value: "17,821"
  - label: WIMD rank (Wales)
    value: "87/1,909"
---

## So what?

- **Crime:** Butetown recorded **17,821** street-level incidents in **36 months** of live police data — far above Cardiff Bay (**6,136**) in the same window, with anti-social behaviour and violence dominating the profile.
- **Deprivation:** **WIMD rank 87/1,909** in Wales (top ~5% most deprived) — entrenched disadvantage across income, employment, education, health, housing, and community safety.
- **What clubs do:** Grassroots sport reaches **hundreds of young people weekly** — boxing, football, and Premier League Kicks programmes address exploitation risk, anti-social behaviour, and lack of opportunity where statutory services fall short.

**[Download one-page executive summary (PDF)](/projects/butetown-community-impact/executive-summary.pdf)** — written for funders, councils, and youth organisations.

## My role & impact

As **Vice-Chairperson at Tiger Bay Youth Development**, I built this report to:

- Brief the **committee and parents** on crime and deprivation context in plain language
- Support **grant and funding conversations** with evidence (e.g. Premier League Kicks, knife-crime programme funding)
- Connect **public data** to programmes I help lead — not abstract analytics, but material we use locally in Butetown

## Problem

Butetown is one of Cardiff's most deprived and highest-crime neighbourhoods — yet the story of how residents respond is often told anecdotally, not with data. Stakeholders needed a clear picture of **crime and deprivation benchmarks** alongside **what community sport organisations are doing** to address exploitation risk, anti-social behaviour, and lack of opportunity for young people.

As Vice-Chairperson at **Tiger Bay Youth Development**, I wanted to connect public data with on-the-ground programmes — showing that sport here is not just recreation, but infrastructure filling gaps left by failures in employment, education, and public safety.

## Data sources

- **Police recorded crime** — Butetown crime rate (260 per 1,000 people), category breakdown, September 2025 incident peak (278)
- **Welsh Index of Multiple Deprivation (WIMD)** — area rank 87 of 1,909 (1 = most deprived); domain scores for income, employment, health, education, housing, community safety
- **WIMD 2025 education report** — Butetown flagged among Cardiff areas with concerning educational outcomes
- **Programme data** — Tiger Bay ABC (~200 youths/week), Tiger Bay FC (est. 2009), AFC Butetown / Cardiff Bay Warriors (est. 2005), Premier League Kicks (£474,928 National Lottery grant, 9 Cardiff sites including Butetown at Cardiff & Vale College)
- **Qualitative research** — club histories, funding sources (Youth Endowment Fund / Home Office knife-crime project), community context (Cardiff Bay gentrification vs Butetown neglect, rail line dividing the area)
- **[data.police.uk API](https://data.police.uk)** — live street-level crimes for Butetown, Cardiff Bay, Grangetown, Riverside, City Centre, and Adamsdown (1-mile radius per point; custom polygon for South Cardiff docklands)

## Data extraction (API & SQL)

Reproducible fetch: `npm run fetch:police` → `scripts/police_api_client.py`.

**REST endpoints used:**

```http
GET https://data.police.uk/api/crimes-street-dates
GET https://data.police.uk/api/crimes-street/all-crime?lat=51.4637&lng=-3.1690&date=2025-09
POST https://data.police.uk/api/crimes-street/all-crime
     body: poly=51.4505,-3.1980:...&date=2025-09
```

Point samples use the Butetown centre; polygon POST covers the **South Cardiff docklands** analysis area.

**SQL layer:** summary data is loaded into `data/portfolio.db` (`crime_monthly`, `crime_categories`). Example queries in `content/code/butetown_police_queries.sql`:

```sql
-- Butetown vs Cardiff Bay — monthly comparison
SELECT b.month, b.crime_count AS butetown, c.crime_count AS cardiff_bay
FROM crime_monthly b
JOIN crime_monthly c ON b.month = c.month AND c.area = 'Cardiff Bay'
WHERE b.area = 'Butetown'
ORDER BY b.month DESC LIMIT 12;
```

Build the database: `npm run db:build`

**Live SQL results:** [View query output on /sql](/sql#butetown) (regenerate with `npm run sql:report`).

## Visual analysis

Charts from `npm run charts:butetown`. Fetch all available API months: `npm run fetch:police` (requests 10 years; API currently returns **36 months**, Apr 2023 – Mar 2026).

### Crime totals by Cardiff area (data.police.uk)

![Street-level crimes compared across Cardiff neighbourhoods](/projects/butetown-community-impact/09-live-crime-by-area.png)

**36 months** of API data for **Butetown** (17,821), **Cardiff Bay** (6,136), **Grangetown**, **Riverside**, **City Centre**, and **Adamsdown** (1-mile radius per point).

### Crime categories — Butetown

![Butetown crime categories from police API](/projects/butetown-community-impact/10-live-butetown-categories.png)

Category breakdown across all available months — led by **anti-social behaviour** and **violence & sexual offences**.

### Monthly trend — Butetown

![Butetown monthly crime trend](/projects/butetown-community-impact/12-ten-year-monthly-trend.png)

Month-by-month counts with a **12-month rolling average** (meaningful once 12+ months exist in the series).

### Yearly totals by area

![Yearly crime totals by Cardiff area](/projects/butetown-community-impact/13-ten-year-yearly-by-area.png)

2023–2026 yearly comparison — Butetown averaged ~5,000+ crimes/year in the API sample vs ~1,500–2,000 for Cardiff Bay.

### Butetown vs Cardiff Bay

![Butetown vs Cardiff Bay monthly comparison](/projects/butetown-community-impact/14-butetown-vs-cardiff-bay.png)

Side-by-side monthly series — relevant to the **gentrified Bay vs neglected Butetown** narrative in the research.

### Geospatial crime map (South Cardiff)

![Geospatial map of street-level crimes near Butetown](/projects/butetown-community-impact/11-crime-geospatial-map.png)

Approximate crime locations (anonymised per police guidelines) across the docklands boundary — **Butetown**, **Cardiff Bay**, and connecting neighbourhoods. Star markers show API sample centres; dashed polygon is the custom South Cardiff analysis area.

**Interactive map:** [Open full-screen crime map](/projects/butetown-community-impact/crime-map.html) — zoom, pan, and click incidents for category and street details (OpenStreetMap + data.police.uk).

### Crime rate vs national benchmarks

![Butetown crime rate compared to Wales and UK averages](/projects/butetown-community-impact/01-crime-rate-comparison.png)

Butetown's rate of **260 crimes per 1,000 people** sits **38% above Wales** and **32% above the England, Wales & Northern Ireland average** — placing it among Cardiff's highest-crime areas.

### Crime categories

![Most common crime types in Butetown](/projects/butetown-community-impact/02-crime-categories.png)

**Violent crime** and **anti-social behaviour** dominate the profile, with property damage also elevated — shaping where prevention programmes must focus.

### Incident trend

![Monthly incident trend with September 2025 peak](/projects/butetown-community-impact/03-incident-trend.png)

**278 incidents** were recorded in September 2025 alone — underscoring urgency for sustained youth engagement, not one-off interventions.

### WIMD deprivation domains

![WIMD domain scores for Butetown](/projects/butetown-community-impact/04-wimd-deprivation.png)

Butetown scores highly across **income, employment, health, education, housing, and community safety** — a multi-dimensional deprivation picture, not a single-factor problem.

### WIMD area rank

![WIMD rank position in Wales](/projects/butetown-community-impact/05-wimd-rank.png)

Ranked **87th of 1,909** areas in Wales (where 1 = most deprived), Butetown sits in the **top ~5% most deprived** communities nationally.

### Community club reach

![Estimated reach of sport programmes](/projects/butetown-community-impact/06-club-reach.png)

Local clubs collectively reach **hundreds of young people weekly** — boxing, football, and Premier League Kicks programmes scale beyond what statutory services alone provide.

### Club founding timeline

![Timeline of community clubs in the area](/projects/butetown-community-impact/07-club-timeline.png)

Grassroots organisations have grown over two decades — from **AFC Butetown (2005)** and **Tiger Bay FC (2009)** to **Tiger Bay ABC (2018)** — filling gaps as regeneration favoured Cardiff Bay over Butetown.

### Analysis summary

![Key metrics and community intervention areas](/projects/butetown-community-impact/08-analysis-summary.png)

## Approach

- Compiled and benchmarked **public crime statistics** against Wales and UK baselines
- Mapped **WIMD deprivation domains** to identify where education and community safety interventions matter most
- Researched **four community sport organisations** and their reach, funding, and programme focus
- Connected **structural context** (gentrification, rail-line divide, Somali community marginalisation) to programme design
- Built **reproducible Python visualisations** for portfolio and stakeholder reporting
- Linked findings to **personal leadership role** at Tiger Bay Youth Development for credibility and local insight

**Source code:** `content/code/butetown_community_analysis.py`

## Key findings

**The problem in numbers**

- Crime rate of **260/1,000** — among Cardiff's highest; violent crime and anti-social behaviour dominate
- **38% above Wales**, **32% above UK** — deprivation and safety challenges are structurally entrenched
- **WIMD rank 87/1,909** — high deprivation across income, employment, health, education, housing, and community safety
- **Two Cardiffs in one** — gentrified Cardiff Bay vs neglected Butetown, physically divided by a rail line

**What the clubs are doing**

- **Tiger Bay Amateur Boxing Club** — ~200 youths/week; sanctuary from exploitation; mental health through sport; **five-year knife crime reduction project** (Youth Endowment Fund / Home Office); culturally sensitive sessions for young Muslim women
- **Tiger Bay FC** — formed 2009 by first/second-generation Somali immigrants after exclusion from other teams; now diverse youth teams serving the community
- **AFC Butetown / Cardiff Bay Warriors** — since 2005; leadership pipeline returning former players to coach untapped local talent
- **Premier League Kicks** — **£474,928** National Lottery-funded programme; free football, mentoring, life skills at Cardiff & Vale College Butetown site

**The bigger picture**

Sport in Butetown is filling gaps in employment, education, and public safety — creating jobs (e.g. Tiger Bay Security), delivering Covid food aid, reducing anti-social behaviour, and giving identity to communities marginalised for decades.

## Outcome

Delivered an **evidence-backed community impact report** — executive PDF, interactive map, SQL-ready police summary, and full chart pack — used for **committee updates, parent briefings, and funding discussions** at Tiger Bay Youth Development. Demonstrates public-data extraction, SQL reporting, and stakeholder-ready storytelling for entry-level analyst and community roles.

## Next steps

- Schedule quarterly `npm run fetch:police` to extend the 10-year series
- Add population denominators for true per-capita rates by LSOA
- Overlay Tiger Bay club locations on the interactive map
- Partner with clubs on impact measurement (attendance, referrals, incidents avoided)
