# ============ AUTHENTICATED API CALL ============
from dotenv import load_dotenv
import os
import requests

# Load secrets
load_dotenv()
token = os.getenv("GITHUB_TOKEN")

# Setup headers (Authorization)
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

# API call
url = "https://api.github.com/user"
response = requests.get(url, headers=headers, timeout=10)

print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("✅ Authenticated successfully!")
    print(f"Logged in as: {data.get('login')}")
    print(f"Name: {data.get('name')}")
    print(f"Public repos: {data.get('public_repos')}")
    
    # Rate limit check
    print("\n=== Rate Limits ===")
    rate_limit_url = "https://api.github.com/rate_limit"
    rate_res = requests.get(rate_limit_url, headers=headers, timeout=10)
    rate_data = rate_res.json()
    
    core = rate_data["resources"]["core"]
    print(f"Limit: {core['limit']} requests/hour")
    print(f"Remaining: {core['remaining']} requests")
else:
    print("❌ Auth failed. Check token.")
