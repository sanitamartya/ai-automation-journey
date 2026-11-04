# ============ MINI PROJECT: GitHub User Info Fetcher ============
import requests


def fetch_github_user(username):
    """Fetch GitHub user info. Returns dict or None on failure."""
    url = f"https://api.github.com/users/{username}"
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 404:
            return None
        
        if response.status_code != 200:
            print(f"⚠️  {username}: API error (status {response.status_code})")
            return None
        
        return response.json()
    
    except requests.exceptions.Timeout:
        print(f"⚠️  {username}: request timed out")
        return None
    
    except requests.exceptions.ConnectionError:
        print(f"⚠️  {username}: connection error")
        return None
    
    except Exception as e:
        print(f"⚠️  {username}: unexpected error — {e}")
        return None


def display_user(user):
    """Print user info in a formatted way."""
    print(f"  Name:      {user.get('name') or 'N/A'}")
    print(f"  Username:  {user['login']}")
    print(f"  Followers: {user['followers']}")
    print(f"  Repos:     {user['public_repos']}")
    print(f"  Location:  {user.get('location') or 'N/A'}")


def main():
    """Main function — fetch and display multiple users."""
    usernames = [
        "torvalds",
        "gvanrossum",
        "this-user-does-not-exist-xyz-123",
        "sindresorhus",
    ]
    
    success_count = 0
    fail_count = 0
    
    print("=" * 50)
    print("GitHub User Info Fetcher")
    print("=" * 50)
    
    for username in usernames:
        print(f"\n🔍 Fetching: {username}")
        print("-" * 50)
        
        user = fetch_github_user(username)
        
        if user:
            display_user(user)
            success_count += 1
        else:
            print(f"  ❌ Could not fetch data for '{username}'")
            fail_count += 1
    
    # Summary
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"  ✅ Success: {success_count}")
    print(f"  ❌ Failed:  {fail_count}")
    print(f"  📊 Total:   {len(usernames)}")


if __name__ == "__main__":
    main()

