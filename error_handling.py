# ============ ERROR HANDLING ============
import requests

def fetch_github_user(username):
    """Fetch GitHub user info with proper error handling."""
    url = f"https://api.github.com/users/{username}"
    
    try:
        # timeout=10 → 10 second ke baad give up
        response = requests.get(url, timeout=10)
        
        # Check status code
        if response.status_code == 404:
            print(f"❌ User '{username}' not found")
            return None
        
        if response.status_code != 200:
            print(f"❌ API error: status {response.status_code}")
            return None
        
        # Parse JSON
        data = response.json()
        return data
    
    except requests.exceptions.Timeout:
        print("❌ Request timed out (server slow or no internet)")
        return None
    
    except requests.exceptions.ConnectionError:
        print("❌ Connection error (check internet)")
        return None
    
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None


# Test 1: Valid user
print("=" * 40)
print("Test 1: Valid user")
print("=" * 40)
user = fetch_github_user("torvalds")
if user:
    print(f"Name: {user['name']}")
    print(f"Followers: {user['followers']}")


# Test 2: Invalid user (404)
print("\n" + "=" * 40)
print("Test 2: Invalid user")
print("=" * 40)
user = fetch_github_user("this-user-does-not-exist-xyz-123")
if user:
    print(f"Name: {user['name']}")
