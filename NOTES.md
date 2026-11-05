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

---

# Day 3 — 2025-11-05

## ✅ What I Completed

- File handling (read/write text and JSON files)
- Learned about `.env` files and `python-dotenv` for secrets management
- Generated GitHub Personal Access Token (PAT)
- Made first authenticated API call (`auth_api.py`)
- Checked rate limits (60 -> 5000 requests/hour)
- Updated `.gitignore` to secure the `.env` file

## 🧠 What I Learned

- **File Handling:** Use `with open(...) as f:` so files close automatically. Use `json.dump()` and `json.load()` for JSON files.
- **Secrets Management:** Never hardcode API keys. Put them in `.env` and load with `python-dotenv`.
- **`.env` vs `.env.example`:** `.env` holds real secrets (ignored by git). `.env.example` is a template (committed to git).
- **Auth Headers:** Use `headers={"Authorization": f"Bearer {token}"}` to make authenticated API requests.
- **Rate Limits:** Unauthenticated GitHub API allows 60 req/hr. Authenticated allows 5000 req/hr.
- **Security:** Always add `.env` to `.gitignore` BEFORE adding real secrets to it.

## ❓ Questions / Confusions

- (Add here if any)

## 🎯 Tomorrow's Focus

- Building a multi-API project (Weather + GitHub dashboard)
- Environment variables in real projects
- Structuring a slightly larger Python script

---

# Day 4 — 2025-11-06

## ✅ What I Completed

- Explored Open-Meteo Weather API (Geocoding + Forecast)
- Built `get_coordinates()` and `get_weather()` functions
- Built `get_github_info()` function with token-based auth
- Integrated multiple APIs (Weather + GitHub) into `dashboard.py`
- Displayed data in a clean, structured terminal dashboard

## 🧠 What I Learned

- **Multi-API Flow:** Output of one function (`coords`) can be the input of another function (`get_weather`).
- **Geocoding API:** Converts city names into latitude/longitude.
- **Graceful Degradation:** Check if `.env` token exists before using headers. If not, fallback to unauthenticated API so the app doesn't crash.
- **Dashboard Structuring:** Grouping API outputs into logical sections with formatting (`=` \* 45) makes CLI output readable.

## ❓ Questions / Confusions

- (Add here if any)

## 🎯 Tomorrow's Focus

- Building a CLI Tool using `argparse` or `sys.argv` (taking city name from the terminal)
- Introduction to `FastAPI` (Turning our dashboard into a real web API)

---

# Day 5 — 2025-11-07

## ✅ What I Completed

- Learned and implemented CLI arguments using `sys.argv` (`cli_dashboard.py`)
- Installed `fastapi` and `uvicorn`
- Created first Web API server (`main.py`)
- Added `/`, `/health`, and `/weather` endpoints
- Understood Query Parameters (e.g., `?city=Mumbai`)

## 🧠 What I Learned

- **CLI Args:** `sys.argv` lets scripts take terminal inputs dynamically.
- **FastAPI:** Express.js equivalent for Python. It makes creating endpoints super easy.
- **Uvicorn:** The server that runs the FastAPI app (`uvicorn main:app --reload`).
- **Query Params:** Passing data via URL (`?city=Delhi`) and catching it in function arguments.
- **Auto Docs:** FastAPI automatically creates interactive documentation at `/docs`.
