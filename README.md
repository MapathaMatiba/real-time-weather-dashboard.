# Real-Time Weather Dashboard 🌦️

This project is a real-time weather data pipeline and dashboard that demonstrates essential data engineering skills, including API integration, data processing, database storage, and visualization.

## Features 🚀
- **Real-Time Weather Data**: Fetches weather data for multiple cities using the OpenWeatherMap API.
- **ETL Pipeline**: Extracts, transforms, and loads weather data into a SQLite database.
- **Interactive Dashboard**: Displays weather trends with dynamic filters for cities and time ranges.
- **Automation**: Scheduler fetches data periodically without manual intervention.
- **Visualization**:
  - Line charts for temperature and humidity trends.
  - Choropleth map for regional representation.

## Tech Stack 🛠️
- **Python**
  - Libraries: `requests`, `pandas`, `SQLAlchemy`, `matplotlib`, `seaborn`, `schedule`, `streamlit`
- **SQLite** for lightweight data storage.
- **Streamlit** for building the interactive dashboard.

## How It Works 🔍

1. **Data Ingestion**: 
   - The `fetch_weather_data.py` script fetches real-time weather data from the OpenWeatherMap API.
   - Data is processed and saved into a SQLite database (`weather_data.db`).

2. **Automation**:
   - The `scheduler.py` script automates data fetching every 10 minutes (or any desired interval) using the `schedule` library.

3. **Visualization**:
   - The `streamlit_app.py` script builds an interactive dashboard using Streamlit.
   - Users can filter data by cities and view weather trends.

## Project Structure 📂

```plaintext
real-time-weather-dashboard/
├── fetch_weather_data.py    # Script to fetch and process weather data
├── scheduler.py             # Script to automate data fetching
├── streamlit_app.py         # Streamlit dashboard for visualization
├── weather_data.db          # SQLite database for storing weather data
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation

Installation and Usage 🛠️
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/real-time-weather-dashboard.git
cd real-time-weather-dashboard
Set Up the Environment:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
Add Your API Key:

Replace your_api_key in fetch_weather_data.py with your OpenWeatherMap API key.
Run the Scripts:

Fetch Weather Data:
bash
Copy code
python fetch_weather_data.py
Automate Data Fetching:
bash
Copy code
python scheduler.py
Run the Dashboard:
bash
Copy code
streamlit run streamlit_app.py
View the Dashboard:

Open http://localhost:8501 in your browser.
Example Visualizations 📊
Temperature Trends

Regional Representation (Heatmap)

Future Enhancements 🔮
Support for additional APIs and weather data metrics.
Deployment to a cloud platform (e.g., Streamlit Cloud, Heroku).
Real-time notifications for significant weather changes.
