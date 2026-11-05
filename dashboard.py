# ============ MULTI-API DASHBOARD (Part 1: Geocoding) ============
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_coordinates(city_name):
    """Fetch latitude and longitude for a given city name."""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"❌ Geocoding API error: {response.status_code}")
            return None
        
        data = response.json()
        
        # Check if results exist (agar city nahi mili toh khali list aayegi)
        if "results" not in data or len(data["results"]) == 0:
            print(f"❌ City '{city_name}' not found.")
            return None
            
        # Extract lat/lon from the first result
        result = data["results"][0]
        lat = result["latitude"]
        lon = result["longitude"]
        
        return {"latitude": lat, "longitude": lon}
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def get_weather(lat, lon):
    """Fetch current weather for given coordinates."""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"❌ Weather API error: {response.status_code}")
            return None
        
        data = response.json()
        
        # Extract weather data
        current = data.get("current_weather")
        if not current:
            print("❌ Weather data not found in response.")
            return None
            
        return {
            "temperature": current["temperature"],
            "windspeed": current["windspeed"]
        }
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def get_github_info(username):
    """Fetch basic GitHub info for a user."""
    url = f"https://api.github.com/users/{username}"
    
    # Agar token available hai to use karo (for higher rate limits)
    headers = {}
    if GITHUB_TOKEN and GITHUB_TOKEN != "your_github_token_here":
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
        
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 404:
            print(f"❌ GitHub user '{username}' not found.")
            return None
        if response.status_code != 200:
            print(f"❌ GitHub API error: {response.status_code}")
            return None
            
        data = response.json()
        return {
            "name": data.get("name") or "N/A",
            "followers": data.get("followers"),
            "repos": data.get("public_repos")
        }
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


# Test the function
# Test both functions
if __name__ == "__main__":
    # Settings for the dashboard
    MY_CITY = "Delhi"
    MY_GITHUB_USERNAME = "sanitamartya" # Apna GitHub username daalna
    
    print("=" * 45)
    print("🚀 MY PERSONAL DASHBOARD")
    print("=" * 45)
    
    # --- WEATHER SECTION ---
    print(f"\n📍 Location: {MY_CITY}")
    coords = get_coordinates(MY_CITY)
    if coords:
        weather = get_weather(coords["latitude"], coords["longitude"])
        if weather:
            print(f"   🌡️  Temp: {weather['temperature']}°C")
            print(f"   💨 Wind: {weather['windspeed']} km/h")
    else:
        print("   ❌ Could not load weather.")
        
    # --- GITHUB SECTION ---
    print(f"\n💻 GitHub Profile: @{MY_GITHUB_USERNAME}")
    github = get_github_info(MY_GITHUB_USERNAME)
    if github:
        print(f"   👤 Name:      {github['name']}")
        print(f"   👥 Followers: {github['followers']}")
        print(f"   📁 Repos:     {github['repos']}")
    else:
        print("   ❌ Could not load GitHub info.")
        
    print("\n" + "=" * 45)

