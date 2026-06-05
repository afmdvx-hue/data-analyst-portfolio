# Go live WITHOUT GitHub

Your project stays on your PC. Vercel uploads it directly.

**No PowerShell?** Use **Command Prompt** (Win + R → `cmd`).

## Step 1 — Open Command Prompt in the project

```cmd
cd /d C:\Users\abdif\data-analyst-portfolio
```

## Step 2 — Log in to Vercel (one time)

```cmd
npx vercel login
```

- Choose **Continue with Email** or **GitHub** (for Vercel login only — you don't need a project on GitHub)
- Finish login in the browser
- When it says success, go back to Command Prompt

## Step 3 — Build and deploy

**Run each line separately** (press Enter after each):

```cmd
set NEXT_PUBLIC_SITE_URL=https://abdifatah.uk
npm run build
npx vercel --prod
```

Do **not** paste two commands on one line (e.g. `vercel --prod$env:...` breaks).

Answer the questions:

| Question | Answer |
|----------|--------|
| Set up and deploy? | **Y** |
| Which scope? | Your account |
| Link to existing project? | **N** (first time) |
| Project name? | Press **Enter** (default is fine) |
| Directory? | Press **Enter** (`.` = current folder) |

Wait until it finishes. It prints a URL like `https://something.vercel.app` — your site is live.

## Step 4 — Add your domain (abdifatah.uk)

1. Go to [vercel.com/dashboard](https://vercel.com/dashboard)
2. Click your project
3. **Settings** → **Domains**
4. Add `abdifatah.uk` and `www.abdifatah.uk`
5. Copy the DNS records Vercel shows into your domain registrar (where you bought `.uk`)
6. **Settings** → **Environment Variables** → add:
   - `NEXT_PUBLIC_SITE_URL` = `https://abdifatah.uk`
7. **Deployments** → **Redeploy** (so the domain env applies)

## Step 5 — Check

Open **https://abdifatah.uk** (after DNS works, can take up to an hour).

---

## Updating the site later (no GitHub)

After you change files locally:

```cmd
cd /d C:\Users\abdif\data-analyst-portfolio
npm run build
npx vercel --prod
```

---

## You do NOT need

- GitHub
- `git push`
- A code repository online

GitHub is optional for the future. Vercel + your PC is enough.
