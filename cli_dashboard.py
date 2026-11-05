# ============ CLI ARGUMENTS ============
import sys
import requests
from dotenv import load_dotenv
import os

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# (Yahan humne pichhle din ke functions copy kiye hain, taaki code chhota lage)
def get_weather(city):
    # Simplified weather fetch for testing
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    res = requests.get(url, timeout=10).json()
    if "results" not in res: return None
    lat, lon = res["results"][0]["latitude"], res["results"][0]["longitude"]
    
    w_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    w_res = requests.get(w_url, timeout=10).json()
    return w_res["current_weather"]

if __name__ == "__main__":
    # Check karo ki user ne arguments diye hain ya nahi
    # sys.argv[0] hamesha file ka naam hota hai (cli_dashboard.py)
    if len(sys.argv) < 3:
        print("❌ Error: Missing arguments!")
        print("Usage: python cli_dashboard.py <city> <github_username>")
        sys.exit(1) # Error code 1 ke saath exit karo
        
    # Arguments extract karo
    # sys.argv[1] = city, sys.argv[2] = github username
    city_arg = sys.argv[1]
    github_arg = sys.argv[2]
    
    print(f"🔍 Fetching data for City: {city_arg} and GitHub: {github_arg}")
    
    # Weather test
    weather = get_weather(city_arg)
    if weather:
        print(f"🌡️  Temp in {city_arg}: {weather['temperature']}°C")
        
    # GitHub logic yahan add mat karo abhi, humne pichhle file mein kar diya hai.
    print("✅ CLI Input successful!")
