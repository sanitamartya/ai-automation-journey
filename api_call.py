# ============ FIRST API CALL ============
import requests

# API endpoint
url = "https://api.github.com/users/torvalds"

# Send GET request
response = requests.get(url)

# Check status code
print("Status code:", response.status_code)

# Parse JSON response into Python dictionary
data = response.json()

# Extract specific fields
print("Name:", data["name"])
print("Username:", data["login"])
print("Followers:", data["followers"])
print("Public repos:", data["public_repos"])
print("Location:", data["location"])
print("Bio:", data["bio"])
