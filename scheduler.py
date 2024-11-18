import schedule
import time
from fetch_weather_data import fetch_weather_data, save_to_database

def job():
    city_list = ["New York", "London", "Tokyo"]
    weather_data = [fetch_weather_data(city) for city in city_list]
    weather_data = [w for w in weather_data if w is not None]
    save_to_database(weather_data)

schedule.every(10).minutes.do(job)

if __name__ == "__main__":
    print("Starting the weather data scheduler...")
    while True:
        schedule.run_pending()
        time.sleep(1)
