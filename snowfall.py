import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def snowfall():
    # Define location details and range of years
    latitude = 37.98381
    longitude = 23.727539
    years = range(2014, 2024)  # Last 10 years

    def fetch_yearly_data(year):
        url = (
            f"https://archive-api.open-meteo.com/v1/archive?"
            f"latitude={latitude}&longitude={longitude}"
            f"&start_date={year}-01-01&end_date={year}-12-31"
            f"&hourly=snowfall&timezone=Europe%2FBerlin"
        )
        response = requests.get(url)
        data = response.json()
        
        # Extract hourly snowfall data
        hourly = data['hourly']
        timestamps = hourly['time']
        snowfall = hourly['snowfall']
        
        # Convert to DataFrame
        df = pd.DataFrame({
            'timestamp': pd.to_datetime(timestamps),
            'snowfall': snowfall
        })
        
        return df

    # Fetch and combine data
    all_data = []
    for year in years:
        print(f"Fetching data for {year}...")
        yearly_df = fetch_yearly_data(year)
        yearly_df['year'] = year
        all_data.append(yearly_df)

    # Combine all yearly data
    df_combined = pd.concat(all_data)

    # Set timestamp as index
    df_combined.set_index('timestamp', inplace=True)

    # Resample to daily data and calculate the daily sum of snowfall
    daily_df = df_combined.resample('D').sum()

    # Plotting
    plt.figure(figsize=(14, 7))
    plt.bar(daily_df.index, daily_df['snowfall'], color='tab:blue', width=1.0, label='DailyAverage Snowfall')
    plt.xlabel('Date')
    plt.ylabel('Snowfall (mm)')
    plt.title('Daily Snowfall for the Last 10 Years\nLocation: Athens, Greece')
    plt.legend()
    plt.grid(axis="y")
    plt.tight_layout()

    
    plt.show()