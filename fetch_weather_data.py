import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

# API configuration
API_KEY = "input-your-API_KEY"  # Replace with your actual API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"  # Fixed the missing scheme

# Function to fetch weather data
def fetch_weather_data(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Get temperature in Celsius
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        # Extract relevant information
        weather = {
            "city": data["name"],
            "datetime": datetime.now(),
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }
        return weather
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data for {city}. Error: {e}")
        return None

# Database setup
engine = create_engine("sqlite:///weather_data.db")

# Function to save data to the database
def save_to_database(data):
    if data:  # Ensure there's data to save
        df = pd.DataFrame(data)
        df.to_sql("weather", engine, if_exists="append", index=False)
        print("Data saved to database.")
    else:
        print("No data to save.")

# Main execution
if __name__ == "__main__":
    city_list = ["New York", "London", "Tokyo"]
    weather_data = [fetch_weather_data(city) for city in city_list]
    weather_data = [w for w in weather_data if w is not None]  # Filter out None values
    save_to_database(weather_data)

