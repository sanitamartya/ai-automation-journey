# Day 1 — 2025-11-03

## ✅ What I Completed

- Python 3.14 verified
- pip installed & upgraded to 26.3
- Created project: `ai-automation-journey`
- Virtual environment set up and activated
- Wrote and ran first Python program (`hello.py`)
- Git + GitHub setup complete
- `.gitignore` configured (venv, cache, secrets ignored)
- First commit pushed to GitHub

## 🧠 What I Learned

- **Virtual environments** isolate project dependencies — no conflicts between projects
- **`.gitignore`** must be set up BEFORE first commit to prevent tracking unwanted files
- **Git workflow:** working dir → staging (`git add`) → commit → push
- **`git commit -m`** flag for inline messages (faster than editor)
- **Commit messages** should be short, present tense, specific
- Linux uses `python3` and `pip3` (unlike Windows `python`/`pip`)

## ❓ Questions / Confusions

- (koi doubt ho to yahan likho)

## 🎯 Tomorrow's Focus

- Python data types (str, int, float, bool)
- Lists & dictionaries
- Functions
- Mini project: Student Grade Calculator

---

# Day 2 — 2025-11-04

## ✅ What I Completed

- Python syntax speedrun (with JS comparison)
- Installed `requests` library
- Created `requirements.txt` (learned: pip freeze must run inside venv)
- First real API call — GitHub API (`api_call.py`)
- Error handling with `try/except` (`error_handling.py`)
- Mini project: Multi-user GitHub info fetcher (`github_fetcher.py`)

## 🧠 What I Learned

- **Python vs JS syntax:** No semicolons, no braces, indentation matters
- **`requests` library:** `requests.get()` is like `fetch()` but synchronous
- **Error handling:** `try/except` with specific exception types (`Timeout`, `ConnectionError`)
- **Always use timeout:** `requests.get(url, timeout=10)` — production best practice
- **Safe dict access:** `user.get("key") or "default"` — like JS `?.` and `??`
- **`if __name__ == "__main__":`** — run code only when file is executed directly
- **Venv lesson:** Always check `(venv)` prefix and `which python` before installing
- **`pip freeze`** must be run inside venv, otherwise system packages get listed

## ❓ Questions / Confusions

- Rate limiting: GitHub allows 60 requests/hour unauthenticated — how to handle in production?
- (add more if any)

## 🎯 Tomorrow's Focus

- File handling (read/write JSON)
- Working with APIs that need auth (API keys)
- `.env` for secrets management
- Small project: Weather + GitHub combined dashboard
