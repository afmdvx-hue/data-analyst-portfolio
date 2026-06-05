# Add this project to GitHub

## 1. Install Git (if needed)

Already attempted via winget. If `git` still fails in terminal, install from [git-scm.com](https://git-scm.com/download/win) and restart Cursor.

## 2. Create an empty repo on GitHub

1. Log in at [github.com](https://github.com)
2. Click **+** → **New repository**
3. Name: `data-analyst-portfolio` (or any name)
4. Leave it **empty** — do **not** add README, .gitignore, or license (you already have those)
5. Click **Create repository**

## 3. Push from your PC

**Already done on your machine:** `git init` and `origin` remote. You only need **commit + push**.

See **`GITHUB-RETRY.md`** for Windows fixes (PowerShell scripts, auth, README conflicts).

```powershell
cd C:\Users\abdif\data-analyst-portfolio

git add .
git commit -m "Initial commit: data analyst portfolio"
git branch -M main
git push -u origin main
```

If `git` is not found, use:

```powershell
& "C:\Program Files\Git\cmd\git.exe" -C "C:\Users\abdif\data-analyst-portfolio" push -u origin main
```

Only run `git remote add origin ...` if `git remote -v` shows nothing.

Your repo URL: **https://github.com/afmdvx-hue/data-analyst-portfolio**

GitHub will ask you to sign in (browser or personal access token).

## 4. Deploy on Vercel (after push)

1. [vercel.com/new](https://vercel.com/new)
2. **Import** your GitHub repo
3. Environment variable: `NEXT_PUBLIC_SITE_URL` = `https://abdifatah.uk`
4. Deploy → then add domain **abdifatah.uk** in Vercel settings

## Do not commit

These are already in `.gitignore`:

- `.env.local` (secrets)
- `node_modules`
- Large police cache files
