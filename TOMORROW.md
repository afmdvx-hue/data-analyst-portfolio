# Pick up — almost done

**Read SETUP-NOW.md** — only Vercel login + DNS left (cannot be automated).

# Pick up tomorrow

## Project location

`C:\Users\abdif\data-analyst-portfolio`

## Start dev server

```bash
cd C:\Users\abdif\data-analyst-portfolio
npm run dev
```

Open http://localhost:3000

## Done recently

- Supply chain, Butetown (hero), pricing case studies
- Hire me strip, professional homepage, `/sql` page
- `public/resume.pdf`, executive PDF for Butetown
- Experience section removed; AI/ML in skills and copy
- Scripts: `predeploy`, `deploy`, `resume`, `sql:report`, `db:build`

## Visitor tracking & email links

- **Admin → Visitors** (`/admin/analytics`) — recent visits + **email-safe link builder**
- Use **`/welcome?utm_source=company_name`** in emails (see `EMAIL-OUTREACH.md`)
- Set `NEXT_PUBLIC_SITE_URL` + `NEXT_PUBLIC_GA_MEASUREMENT_ID` in `.env.local`

## Tomorrow priority list

1. **Deploy** — `npm run predeploy` then `npm run deploy` — connect **abdifatah.uk** in Vercel (see `DEPLOY.md`)
2. **GitHub** — init/push repo, add URL to `content/site.json` → `social.github`
3. **CV** — regenerate after deploy URL: `npm run resume`
4. **Applications** — Indeed, Reed, CV-Library with portfolio link (no LinkedIn required)
5. Optional: recruiter emails + Cardiff speculative (council, charities) with Butetown PDF

## Quick commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | Local site |
| `npm run predeploy` | DB + SQL JSON + PDFs |
| `npm run deploy` | Vercel production |
| `npm run fetch:police` | Refresh crime data |
| `npm run charts:butetown` | Refresh charts |

## Contact on site

- Email: afm.dvx@gmail.com
- Phone: 07869731897
- CV: `/resume.pdf`
