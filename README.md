# Final Project
# Weather Service (Backend)

REST API microservice that returns current weather for 4 predefined locations using OpenWeatherMap.

## Supported locations
- `newyork` -> New York
- `sydney` -> Sydney
- `capetown` -> Cape Town
- `bangkok` -> Bangkok

## Prerequisites
Set environment variable:
- `OPENWEATHER_API_KEY` (get it from OpenWeatherMap)

## Run locally (no Docker)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

export OPENWEATHER_API_KEY="YOUR_KEY"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

