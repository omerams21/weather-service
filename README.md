# Weather Service (Backend)

A Flask-based REST API microservice that fetches current weather data from OpenWeatherMap
for predefined locations.

## Supported Locations
Use the following `location_key` values:
- newyork  -> New York
- sydney   -> Sydney
- capetown -> Cape Town
- bangkok  -> Bangkok

## OpenWeatherMap API Key Setup
1. Create a free API key at:
   https://openweathermap.org/api

2. In Linux / WSL, set the API key as an environment variable:
   export OPENWEATHER_API_KEY="YOUR_API_KEY"

The API key is required for the backend to communicate with OpenWeatherMap.

## Run Locally (Linux / WSL, No Docker)
1. Navigate to the backend repository:
   cd weather-service

2. Create and activate a virtual environment:
   python3 -m venv .venv
   source .venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Set the API key and run the server:
   export OPENWEATHER_API_KEY="YOUR_API_KEY"
   python app/app.py

The backend will be available at:
http://localhost:5000

## Run with Docker
1. Build the Docker image:
   docker build -t weather-service:flask .

2. Run the container:
   docker run --rm -p 5000:5000 \
     -e OPENWEATHER_API_KEY="YOUR_API_KEY" \
     weather-service:flask

## API Endpoints

### Get Weather by Location Key
GET /weather/<location_key>
The endpoint returns a JSON response with temperature, description, humidity and wind speed.

Example:
curl http://localhost:5000/weather/newyork

Example response:
{
  "location_key": "newyork",
  "city": "New York",
  "temperature_c": 12.3,
  "description": "clear sky",
  "humidity": 44,
  "wind_speed": 4.6
}

### Health Check
GET /health

Example:
curl http://localhost:5000/health

