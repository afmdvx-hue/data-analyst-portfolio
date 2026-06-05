# Portfolio agents

This repo has three ways to manage data analyst case studies.

## Professional Project Improver (recommended)

**URL:** `/admin/improver` (local dev only)

Connects to data analyst repositories, syncs analysis code, audits every case study, and applies professional improvements.

### Workflow

1. Add GitHub URLs or local folder paths in `content/repos.json`
2. Open `/admin/improver` or type `repos` in the file terminal
3. Click **Sync repos → code → case studies**
4. Review quality scores and click **Improve all** or improve individual projects
5. For deep rewrites, use the Cursor **professional-project-improver** skill

### CLI

```bash
npm run sync-repos          # Pull repos → content/code → case studies
npm run audit-projects      # Score all projects
npm run audit-projects -- --fix   # Apply auto-fixes
```

---

## Project Builder Agent (in-app)

**URL:** `/admin/builder` (local dev only)

A guided conversational agent that walks through:

1. Title and summary
2. Business problem
3. Data sources
4. Tools (SQL, Python, Tableau, etc.)
5. Approach and methodology
6. Key findings and impact metrics
7. Outcome and next steps

It publishes a markdown file to `content/projects/` automatically.

## File Terminal

**URL:** `/admin`

Upload existing `.md` files or run `npm run add-project <slug>` from the CLI.

Commands: `repos`, `improve`, `improver`, `sync`, `upload`, `list`

---

## Cursor: Professional Project Improver

When the user asks to **improve, polish, professionalize, or upgrade a portfolio project or data analyst case study**, act as the **Professional Project Improver** agent.

### Your job

Take existing projects (markdown case studies + linked code in `content/code/`) and elevate them to hiring-manager quality — the same standard as `pricing-analytics.md` and `butetown-community-impact.md`.

### Before editing

1. Read `content/site.json` for owner context
2. Read `content/repos.json` for linked repositories
3. Run `npm run audit-projects` or read issues via `/api/portfolio/improve`
4. Read the target project in `content/projects/` and any linked code in `content/code/`
5. Read 1–2 existing high-quality projects for tone reference

### Repository connection

- Configure repos in `content/repos.json` (`url` for GitHub, or `localPath` for local folders)
- Run `npm run sync-repos` to pull `.py`, `.ipynb`, `.sql` into `content/code/`
- Link source code in the Approach section: `**Source code:** \`content/code/filename.py\``

### Professional quality bar

Every case study must have:

| Criterion | Standard |
|-----------|----------|
| Description | One line, business impact first, 60–200 chars |
| Problem | Stakeholders, decision context, why it mattered |
| Data sources | Specific tables, APIs, exports — not placeholders |
| Approach | Named techniques (joins, cohorts, regression, geospatial filter) |
| Key findings | Numbered insights with quantified results |
| Outcome | Decisions made, dashboards delivered, time/money saved |
| Metrics | 1–3 YAML metrics with real values |

### Improvement checklist

```
- [ ] Remove all placeholder text ("Describe the business question…")
- [ ] Add or refine impact metrics in frontmatter
- [ ] Ensure findings include numbers (%, counts, $, R², elasticity)
- [ ] Reference linked code and chart scripts where relevant
- [ ] Match tone of best existing projects — confident, specific, stakeholder-aware
- [ ] Tags and tools reflect actual stack from code imports
- [ ] Description leads with outcome, not tool names
```

### Do not

- Invent fake companies or inflated metrics without user confirmation
- Add LinkedIn links (user preference)
- Change unrelated site layout unless asked
- Downgrade projects that already meet the quality bar

---

## Cursor: Data Analyst Project Builder

When the user asks to **create or add a new portfolio project / case study**, act as a **Data Analyst Project Builder** agent.

### Case study structure (required)

Every project must include YAML frontmatter:

```yaml
---
title: ...
slug: ...
description: ...        # one line for cards + SEO
date: "YYYY-MM-DD"
featured: true|false
tags: [...]
tools: [...]
metrics:
  - label: ...
    value: ...
---
```

Body sections: Problem, Data sources, Approach, Key findings, Outcome, Next steps (optional).

See existing projects in `content/projects/` for style reference.
