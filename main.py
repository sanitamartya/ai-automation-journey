# ============ PEHLA FASTAPI SERVER ============
import requests
from fastapi import FastAPI

# 1. App create karo
app = FastAPI(
    title="My AI Automation API",
    description="Learning FastAPI step-by-step"
)

# 2. Home endpoint (Root route)
@app.get("/")
def home():
    return {
        "message": "Welcome to my API!",
        "status": "success",
        "day": 5
    }

# 3. Ek aur endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "server": "running"
    }

@app.get("/weather")
def get_weather(city: str):
    # 1. Coordinates fetch karo
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    
    try:
        geo_res = requests.get(geo_url, timeout=10).json()
        
        # Agar city nahi mili
        if "results" not in geo_res or len(geo_res["results"]) == 0:
            return {"error": f"City '{city}' not found"}
            
        lat = geo_res["results"][0]["latitude"]
        lon = geo_res["results"][0]["longitude"]
        
        # 2. Weather fetch karo
        w_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        w_res = requests.get(w_url, timeout=10).json()
        
        return {
            "city": city,
            "latitude": lat,
            "longitude": lon,
            "temperature": w_res["current_weather"]["temperature"],
            "windspeed": w_res["current_weather"]["windspeed"]
        }
        
    except Exception as e:
        return {"error": str(e)}
