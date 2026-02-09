import os
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="Weather Service", version="1.0.0")

LOCATION_MAP = {
    "newyork": "New York",
    "sydney": "Sydney",
    "capetown": "Cape Town",
    "bangkok": "Bangkok",
}

OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/weather/{location_key}")
def get_weather(location_key: str):
    if location_key not in LOCATION_MAP:
        raise HTTPException(
            status_code=404,
            detail=f"Unknown location_key '{location_key}'. Allowed: {list(LOCATION_MAP.keys())}",
        )

    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="Server is missing OPENWEATHER_API_KEY")

    city = LOCATION_MAP[location_key]
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        r = requests.get(OPENWEATHER_URL, params=params, timeout=10)
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Upstream request failed: {str(e)}")

    if r.status_code != 200:
        try:
            err = r.json()
        except Exception:
            err = {"message": r.text}
        raise HTTPException(status_code=502, detail={"upstream_status": r.status_code, "upstream_error": err})

    data = r.json()

    return {
        "location_key": location_key,
        "city": city,
        "temperature_c": data.get("main", {}).get("temp"),
        "description": (data.get("weather") or [{}])[0].get("description"),
        "humidity": data.get("main", {}).get("humidity"),
        "wind_speed": data.get("wind", {}).get("speed"),
    }
