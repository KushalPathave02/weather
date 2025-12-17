import json

# Dummy weather data
DUMMY_WEATHER_DATA = {
    "pune": {"temperature": 24, "condition": "Clear"},
    "mumbai": {"temperature": 28, "condition": "Humid"},
    "london": {"temperature": 12, "condition": "Cloudy"},
}

def get_weather(city: str) -> str:
    """Fetches the weather for a given city."""
    city_lower = city.lower()
    if city_lower in DUMMY_WEATHER_DATA:
        return json.dumps(DUMMY_WEATHER_DATA[city_lower])
    else:
        return json.dumps({"error": f"Weather data for {city} not found."})
