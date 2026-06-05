# Security

This portfolio implements defence-in-depth for a public Next.js site.

## Checklist

| Control | Implementation |
|--------|----------------|
| HTTPS | `Strict-Transport-Security` in production; middleware redirects HTTP → HTTPS behind proxies |
| CSP | `Content-Security-Policy` via `src/lib/security/headers.ts` + middleware |
| Security headers | `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy` |
| Cloudflare Turnstile | Contact form (`/api/contact`) + `@marsidev/react-turnstile` |
| Input validation | `src/lib/security/validation.ts` — sanitise text, email, slugs, filenames |
| Rate limiting | Middleware (120 req/min/IP on `/api/*`); stricter limits on contact (5/min) |
| Secrets in env | `.env.local` only — see `.env.example`; never commit real keys |
| Dependency updates | `npm run security:audit` |
| Hide sensitive files | `.gitignore`, middleware blocks `/.env`, `/data/`, `.db`, `.pem` |

## Admin APIs

`/api/portfolio/*` routes return **403 in production** (`NODE_ENV !== development`). Edit content via git and redeploy.

## Setup Turnstile

1. Cloudflare dashboard → Turnstile → Add site
2. Copy site key → `NEXT_PUBLIC_TURNSTILE_SITE_KEY`
3. Copy secret → `TURNSTILE_SECRET_KEY` in `.env.local`
4. Restart `npm run dev`

## Optional email delivery

Set `RESEND_API_KEY`, `RESEND_FROM_EMAIL`, and `CONTACT_NOTIFY_EMAIL`. Without these, the form works in development (console log) and returns 503 in production with a mailto fallback.

## Deploy on Cloudflare / Vercel

- Add env vars in the hosting dashboard (not in git)
- Enable **Full (strict)** SSL on Cloudflare if using Cloudflare proxy
- Turnstile works on any HTTPS origin; add your production domain in Turnstile allowed hostnames

## Maintenance

```bash
npm run security:audit   # npm audit (moderate+)
npm update               # bump dependencies periodically
```
