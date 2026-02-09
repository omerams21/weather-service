Weather Service (Backend)

REST API microservice that returns current weather data for predefined locations using the OpenWeatherMap API.

Supported locations
- newyork -> New York
- sydney -> Sydney
- capetown -> Cape Town
- bangkok -> Bangkok

Prerequisites
- Python 3.10+
- OpenWeatherMap API key

Create a free API key at:
https://openweathermap.org/api

Set the environment variable:
export OPENWEATHER_API_KEY="YOUR_API_KEY"

Installation
Clone the repository and install dependencies:
git clone <repository-url>
cd weather-service
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Run locally (no Docker)
export OPENWEATHER_API_KEY="YOUR_API_KEY"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

API documentation will be available at:
http://localhost:8000/docs

Run with Docker
docker build -t weather-service:latest .
docker run --rm -p 8000:8000 -e OPENWEATHER_API_KEY="YOUR_API_KEY" weather-service:latest

API Example
curl http://localhost:8000/weather/newyork

Example response:
{
  "location_key": "newyork",
  "city": "New York",
  "temperature_c": -3.88,
  "description": "clear sky",
  "humidity": 44,
  "wind_speed": 4.63
}

