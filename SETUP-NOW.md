# Finish setup — 3 steps (~15 minutes)

Everything else is **done** in the project (build, PDFs, domain in code, security, analytics).

---

## Step 1 — Put the site online (Vercel)

**Option A — Browser (easiest)**

1. Push this folder to **GitHub** (new repo `data-analyst-portfolio`).
2. Go to [vercel.com/new](https://vercel.com/new) → Import the repo.
3. Before Deploy, add **Environment Variable**:
   - Name: `NEXT_PUBLIC_SITE_URL`
   - Value: `https://abdifatah.uk`
4. Click **Deploy**.

**Option B — CLI**

1. In terminal, run: `npx vercel login` and complete the browser login.
2. Then:
   ```powershell
   cd C:\Users\abdif\data-analyst-portfolio
   $env:NEXT_PUBLIC_SITE_URL="https://abdifatah.uk"
   npx vercel --prod --yes
   ```
3. In [vercel.com](https://vercel.com) → your project → **Settings → Environment Variables** → add `NEXT_PUBLIC_SITE_URL` = `https://abdifatah.uk` → **Redeploy**.

---

## Step 2 — Connect abdifatah.uk

1. Vercel project → **Settings** → **Domains**.
2. Add: `abdifatah.uk` and `www.abdifatah.uk`.
3. At your **domain registrar** (where you bought `.uk`), add the DNS records Vercel shows.

Common pattern:

| Type | Host | Value |
|------|------|--------|
| A | `@` | `76.76.21.21` |
| CNAME | `www` | `cname.vercel-dns.com` |

Use the **exact** values from your Vercel dashboard if they differ.

Wait 5–60 minutes, then open **https://abdifatah.uk**

---

## Step 3 — Use in applications

- **Portfolio URL:** https://abdifatah.uk  
- **Email link (recommended):** https://abdifatah.uk/welcome?utm_source=company_name&utm_medium=email  
- **CV:** https://abdifatah.uk/resume.pdf  

Email signature:

```
Abdifatah Mohamed · Junior Data Analyst
https://abdifatah.uk · Cardiff, UK
afm.dvx@gmail.com · 07869731897
```

---

## Optional (later)

| Task | How |
|------|-----|
| Track visitors | Admin → Visitors locally; add `NEXT_PUBLIC_GA_MEASUREMENT_ID` on Vercel for production |
| Contact form | Cloudflare Turnstile keys in Vercel env (see `.env.example`) |
| GitHub on site | Add URL to `content/site.json` → `social.github` |

---

## Already completed in the repo

- [x] Production build passes (`npm run build`)
- [x] CV PDF with https://abdifatah.uk
- [x] All charts & SQL results
- [x] Domain in `.env.local`, sitemap, Open Graph, email outreach docs
- [x] Security headers, Turnstile-ready contact form
- [x] www → abdifatah.uk redirect in `vercel.json`
