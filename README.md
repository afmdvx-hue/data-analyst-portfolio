# Data Analyst Portfolio

A content-driven portfolio built with **Next.js**, **TypeScript**, and **Tailwind CSS**. Update your profile and case studies without touching layout code.

## Quick start

```bash
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

### Security

See **[SECURITY.md](./SECURITY.md)** — HTTPS headers, CSP, Turnstile contact form, rate limiting, and env-based secrets. Copy `.env.example` → `.env.local` for Turnstile keys.

### Visitor tracking & email-safe links

- **Admin → Visitors** (`/admin/analytics`) — who opened the site + per-company link builder
- Use **`/welcome?utm_source=company_name`** in emails (reduces Gmail warnings) — see **[EMAIL-OUTREACH.md](./EMAIL-OUTREACH.md)**
- Set `NEXT_PUBLIC_SITE_URL` (custom domain) and `NEXT_PUBLIC_GA_MEASUREMENT_ID` (Google Analytics)

### Analyst scripts

| Command | Purpose |
|---------|---------|
| `npm run fetch:police` | Pull data.police.uk crimes into `data/police/` |
| `npm run fetch:supply-chain` | Download Kaggle supply chain CSV |
| `npm run db:build` | Build `data/portfolio.db` for SQL demos |
| `npm run report:butetown` | One-page executive summary PDF |
| `npm run resume` | One-page CV PDF → `public/resume.pdf` |
| `npm run sql:report` | Export SQL tables → `content/sql-results.json` |
| `npm run predeploy` | Build DB, SQL, PDFs before deploy |
| `npm run deploy` | Production build + Vercel deploy |
| `npm run charts:butetown` | Regenerate Butetown charts |
| `npm run charts:supply-chain` | Regenerate supply chain charts |
| `npm run charts:pricing` | Regenerate NYC pricing charts |

### Add files via the terminal UI

While `npm run dev` is running, open **[http://localhost:3000/admin](http://localhost:3000/admin)**:

- Type `help`, `list`, `upload`, or `template`
- **Drag and drop** `.md` project files or images/PDF onto the terminal
- `.md` → saved to `content/projects/`
- `.pdf`, `.png`, `.jpg` → saved to `public/` (resume, screenshots)

Or from your system terminal:

```bash
npm run add-project my-new-project
```

### Project Builder Agent (guided case studies)

Open **[http://localhost:3000/admin/builder](http://localhost:3000/admin/builder)** for a step-by-step agent that asks data-analyst questions (problem, data sources, SQL/Python approach, metrics, outcomes) and publishes a case study to `content/projects/`.

Also available from the admin terminal: type `builder`.

> The web file manager only works locally (`npm run dev`). On Vercel/production, add files in git and redeploy.

## How to update content

### Profile, skills, and experience

Edit **`content/site.json`** — name, bio, skills, job history, social links, and resume URL.

### Add a new project / case study

1. Create a new file in **`content/projects/`**, e.g. `my-new-project.md`
2. Add frontmatter at the top:

```yaml
---
title: My New Project
slug: my-new-project
description: One-line summary for cards and SEO.
date: "2025-01-15"
featured: true
tags: ["SQL", "Tableau"]
tools: ["PostgreSQL", "Tableau"]
metrics:
  - label: Impact metric
    value: "42%"
---

## Problem
Your write-up in Markdown...
```

3. Save — the site picks it up automatically on rebuild (dev server hot-reloads).

### Resume

Drop your PDF at **`public/resume.pdf`** (or change `resumeUrl` in `site.json`).

## Deploy

Push to GitHub and deploy free on [Vercel](https://vercel.com) — zero config for Next.js.

## Project structure

```
content/
  site.json           ← your profile (edit often)
  projects/*.md       ← case studies (add files anytime)
src/
  app/                ← pages
  components/         ← UI sections
  lib/content.ts      ← reads content at build time
```

## Why this stack?

- **Markdown case studies** — easy to write and version in git
- **JSON site config** — quick edits to skills, jobs, and links
- **Next.js** — fast, deployable anywhere, room to grow (blog, analytics, contact form)
