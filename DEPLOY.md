# Deploy to Vercel — abdifatah.uk

Your domain: **https://abdifatah.uk**

## 1. Deploy the site

```bash
npm run predeploy
npm run deploy
```

Or connect the GitHub repo at [vercel.com/new](https://vercel.com/new).

## 2. Add domain in Vercel

1. Vercel project → **Settings** → **Domains**
2. Add `abdifatah.uk` and `www.abdifatah.uk`
3. Vercel shows DNS records to add at your registrar

Typical setup:

| Type | Name | Value |
|------|------|--------|
| **A** | `@` | `76.76.21.21` (Vercel — confirm in dashboard) |
| **CNAME** | `www` | `cname.vercel-dns.com` |

If your registrar supports **apex ALIAS/ANAME**, follow Vercel’s exact instructions for `.uk` domains.

## 3. Environment variables (Vercel dashboard)

| Variable | Value |
|----------|--------|
| `NEXT_PUBLIC_SITE_URL` | `https://abdifatah.uk` |

Optional: `NEXT_PUBLIC_GA_MEASUREMENT_ID`, Turnstile keys, `RESEND_API_KEY` — see `.env.example`.

Redeploy after adding env vars.

## 4. Regenerate CV

```bash
npm run resume
```

Commit `public/resume.pdf` if you track it in git.

## 5. Email outreach links

Use the **welcome** link per company (Admin → Visitors):

```
https://abdifatah.uk/welcome?utm_source=company_name&utm_medium=email
```

See **EMAIL-OUTREACH.md**.

## 6. Google Search Console

1. [search.google.com/search-console](https://search.google.com/search-console)
2. Add property `https://abdifatah.uk`
3. Verify via DNS TXT or HTML tag (`NEXT_PUBLIC_GSC_VERIFICATION` in Vercel env)

## Notes

- `.env.local` already sets `NEXT_PUBLIC_SITE_URL=https://abdifatah.uk` for local builds
- Admin routes (`/admin`) are **dev-only**; production is read-only
- SSL is automatic on Vercel once DNS propagates (often 5–60 minutes)
