# GitHub + Vercel — Command Prompt only (no PowerShell)

Press **Win + R**, type `cmd`, press Enter.

---

## Step 1 — Open the project folder

```cmd
cd /d C:\Users\abdif\data-analyst-portfolio
```

---

## Step 2 — GitHub empty repo

1. [github.com/new](https://github.com/new)
2. Name: `data-analyst-portfolio`
3. Owner: `afmdvx-hue`
4. **Do not** tick README, .gitignore, or license
5. Create repository

---

## Step 3 — Commit and push

Run each line, press Enter after each:

```cmd
git add .
```

```cmd
git commit -m "Initial commit: junior data analyst portfolio"
```

```cmd
git branch -M main
```

```cmd
git push -u origin main
```

Sign in in the browser or use username `afmdvx-hue` and a **Personal Access Token** as the password.

If `git` is not recognized:

```cmd
"C:\Program Files\Git\cmd\git.exe" add .
"C:\Program Files\Git\cmd\git.exe" commit -m "Initial commit: junior data analyst portfolio"
"C:\Program Files\Git\cmd\git.exe" push -u origin main
```

---

## Step 4 — If push fails (README on GitHub)

Delete the repo and make a new **empty** one, then run `git push` again.

Or:

```cmd
git pull origin main --allow-unrelated-histories
git push -u origin main
```

---

## Step 5 — Vercel (in the browser)

1. [vercel.com/new](https://vercel.com/new)
2. Import `afmdvx-hue/data-analyst-portfolio`
3. Add env: `NEXT_PUBLIC_SITE_URL` = `https://abdifatah.uk`
4. Deploy
5. Settings → Domains → `abdifatah.uk` and `www.abdifatah.uk`

---

## Later updates (cmd)

```cmd
cd /d C:\Users\abdif\data-analyst-portfolio
git add .
git commit -m "Update portfolio"
git push
```

---

## Optional: local build (cmd)

```cmd
cd /d C:\Users\abdif\data-analyst-portfolio
set NEXT_PUBLIC_SITE_URL=https://abdifatah.uk
npm run build
```

No PowerShell needed.
