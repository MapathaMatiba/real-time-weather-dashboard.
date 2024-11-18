import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sqlalchemy import create_engine

# Load data from the database
engine = create_engine("sqlite:///weather_data.db")

def load_data():
    query = "SELECT * FROM weather"
    df = pd.read_sql(query, engine)
    df["datetime"] = pd.to_datetime(df["datetime"])
    return df

# Streamlit app
st.title("Real-Time Weather Dashboard")
st.sidebar.header("Filters")

df = load_data()

# Filter by city
cities = st.sidebar.multiselect("Select Cities", options=df["city"].unique(), default=df["city"].unique())
filtered_df = df[df["city"].isin(cities)]

# Display data
st.subheader("Current Weather Data")
st.write(filtered_df)

# Plot temperature trends
st.subheader("Temperature Trends")
plt.figure(figsize=(10, 5))
for city in cities:
    city_data = filtered_df[filtered_df["city"] == city]
    plt.plot(city_data["datetime"], city_data["temperature"], label=city)
plt.legend()
plt.title("Temperature Over Time")
plt.xlabel("Datetime")
plt.ylabel("Temperature (°C)")
st.pyplot(plt)

# Plot humidity trends
st.subheader("Humidity Trends")
sns.lineplot(data=filtered_df, x="datetime", y="humidity", hue="city")
st.pyplot(plt)
