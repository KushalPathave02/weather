import json
import requests

GEOCODING_API_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"

# WMO Weather interpretation codes
WMO_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Drizzle: Light intensity",
    53: "Drizzle: Moderate intensity",
    55: "Drizzle: Dense intensity",
    56: "Freezing Drizzle: Light intensity",
    57: "Freezing Drizzle: Dense intensity",
    61: "Rain: Slight intensity",
    63: "Rain: Moderate intensity",
    65: "Rain: Heavy intensity",
    66: "Freezing Rain: Light intensity",
    67: "Freezing Rain: Heavy intensity",
    71: "Snow fall: Slight intensity",
    73: "Snow fall: Moderate intensity",
    75: "Snow fall: Heavy intensity",
    77: "Snow grains",
    80: "Rain showers: Slight intensity",
    81: "Rain showers: Moderate intensity",
    82: "Rain showers: Violent intensity",
    85: "Snow showers: Slight intensity",
    86: "Snow showers: Heavy intensity",
    95: "Thunderstorm: Slight or moderate",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}

def degrees_to_cardinal(d):
    """Converts degrees to a cardinal direction."""
    dirs = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    ix = round(d / (360. / len(dirs)))
    return dirs[ix % len(dirs)]

# Fetches and formats real-time weather data for a given city.
def get_weather(city: str) -> str:
    """Fetches the real-time weather for a given city."""
    try:
        # Step 1: Geocode the city
        geo_params = {"name": city, "count": 1}
        geo_res = requests.get(GEOCODING_API_URL, params=geo_params)
        geo_data = geo_res.json()

        if not geo_data.get("results"):
            return f"Error: Could not find location for {city}."

        location = geo_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        name = location.get("name", city)

        # Step 2: Get the weather
        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,weather_code,wind_speed_10m,wind_direction_10m,wind_gusts_10m,wind_speed_80m",
        }
        weather_res = requests.get(WEATHER_API_URL, params=weather_params)
        weather_data = weather_res.json()
        current_weather = weather_data.get("current", {})

        if not current_weather:
            return f"Error: Could not retrieve weather data for {name}."

        # Step 3: Format the response
        temp = current_weather.get("temperature_2m")
        wind_speed_10m = current_weather.get("wind_speed_10m")
        wind_speed_80m = current_weather.get("wind_speed_80m")
        wind_direction_10m = current_weather.get("wind_direction_10m")
        wind_gusts_10m = current_weather.get("wind_gusts_10m")
        weather_code = current_weather.get("weather_code")
        condition = WMO_CODES.get(weather_code, "Unknown condition")
        cardinal_direction = degrees_to_cardinal(wind_direction_10m)

        return (
            f"Current weather in {name}: "
            f"Temperature is {temp}°C with '{condition}'. "
            f"The wind at 10m is {wind_speed_10m} km/h from the {cardinal_direction} ({wind_direction_10m}°), with gusts up to {wind_gusts_10m} km/h. "
            f"At 80m, the wind speed is {wind_speed_80m} km/h."
        )

    except requests.exceptions.RequestException as e:
        return f"Error: API request failed: {e}"
    except Exception as e:
        return f"Error: An unexpected error occurred: {e}"
