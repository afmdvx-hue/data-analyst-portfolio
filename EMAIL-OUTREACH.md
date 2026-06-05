# Email outreach — avoid Gmail “dangerous link” warnings

Gmail flags links when the **domain is new**, **shared** (e.g. `*.vercel.app`), or the email looks like phishing. Use these steps.

## 1. Use a custom domain (most important)

- Buy a domain (e.g. `abdifatah.dev` or `abdimohamed.co.uk`)
- Your domain: **`https://abdifatah.uk`** (configured in `.env.local` / Vercel env)
- Send application emails from the **same domain** (Google Workspace) with SPF/DKIM/DMARC

Avoid sending `https://random-name.vercel.app` in cold emails.

## 2. Use the welcome link in emails (built into admin)

Open **Admin → Visitors** and copy the **welcome link** for each company:

```
https://abdifatah.uk/welcome?utm_source=cardiff_council&utm_medium=email
```

The `/welcome` page explains the site before the homepage — safer for humans and filters.

## 3. Write the email like a human

- Put your **full name** in the subject
- Include the URL as **plain text** (not only a button)
- One sentence: *“This is my data analyst portfolio — case studies include SQL and Cardiff community work.”*
- Do **not** use bit.ly or other shorteners

## 4. Track which company clicked

Each company gets a unique `utm_source` in the link builder. View in:

- **Admin → Visitors** (local log)
- **Google Analytics** → Traffic acquisition (after setting `NEXT_PUBLIC_GA_MEASUREMENT_ID`)

## 5. Technical trust signals (already on site)

- HTTPS + security headers
- `/welcome` landing page
- `sitemap.xml`, `robots.txt`, `humans.txt`, `security.txt`
- Open Graph metadata (set `NEXT_PUBLIC_SITE_URL`)

## 6. Register the site

- [Google Search Console](https://search.google.com/search-console) — verify domain
- Optional: [Bing Webmaster Tools](https://www.bing.com/webmasters)

## Sample email paragraph

> Hi [Name],  
> I’m applying for the Junior Data Analyst role. My portfolio is here:  
> https://abdifatah.uk/welcome?utm_source=your_company&utm_medium=email  
> It includes SQL query results, Python case studies, and a one-page CV.  
> Best regards,  
> Abdifatah Mohamed
