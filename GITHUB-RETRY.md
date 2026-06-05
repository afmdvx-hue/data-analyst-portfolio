# GitHub + Vercel — try again (Windows)

**No PowerShell?** Use **`GITHUB-CMD.md`** — Command Prompt only.

Your repo folder is ready. Remote is already set:

**https://github.com/afmdvx-hue/data-analyst-portfolio**

---

## Before you start

1. Open **Command Prompt** (Win + R → `cmd` → Enter), not PowerShell.
2. Use **full path** if `git` is not found:

   ```cmd
   "C:\Program Files\Git\cmd\git.exe" --version
   ```

---

## Step 1 — GitHub repo (website)

1. Go to [github.com/new](https://github.com/new)
2. Repository name: **`data-analyst-portfolio`**
3. Owner: **`afmdvx-hue`**
4. **Empty repo** — do **not** tick README, .gitignore, or license
5. Create repository

If you already created it **with** a README, delete that repo and make a new empty one, **or** use the “repo already has commits” fix in Step 3 below.

---

## Step 2 — First commit and push

Run **one line at a time** in PowerShell:

```powershell
cd C:\Users\abdif\data-analyst-portfolio
```

```powershell
git add .
```

```powershell
git commit -m "Initial commit: junior data analyst portfolio"
```

```powershell
git branch -M main
```

```powershell
git push -u origin main
```

Sign in when Git asks (browser window or GitHub username + **Personal Access Token** as password).

---

## Step 3 — If push fails

### “rejected” / “fetch first” / README on GitHub

You created the repo **with** a README. Either:

**A — Empty repo (easiest):** Delete repo on GitHub → create new **empty** repo → run `git push -u origin main` again.

**B — Keep repo with README:**

```powershell
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### “Authentication failed”

1. GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Generate token with scope **`repo`**
3. On push, password = **paste the token** (not your GitHub password)

### `git` not recognized

```powershell
& "C:\Program Files\Git\cmd\git.exe" -C "C:\Users\abdif\data-analyst-portfolio" push -u origin main
```

---

## Step 4 — Vercel from GitHub

1. [vercel.com/new](https://vercel.com/new)
2. **Import Git Repository** → choose **`afmdvx-hue/data-analyst-portfolio`**
3. Framework: **Next.js** (auto-detected)
4. **Environment variable:**

   | Name | Value |
   |------|--------|
   | `NEXT_PUBLIC_SITE_URL` | `https://abdifatah.uk` |

5. **Deploy**
6. **Settings → Domains** → add `abdifatah.uk` and `www.abdifatah.uk` → DNS at your registrar

Every `git push` to `main` will redeploy automatically.

---

## Later updates

```powershell
cd C:\Users\abdif\data-analyst-portfolio
git add .
git commit -m "Update portfolio content"
git push
```
