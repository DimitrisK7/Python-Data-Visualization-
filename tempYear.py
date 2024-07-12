import requests
import pandas as pd
import matplotlib.pyplot as plt


def tempYear():
    latitude = 37.98381
    longitude = 23.727539

    # The URL for the API request - 
    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={latitude}&longitude={longitude}"
        f"&start_date=2023-06-26&end_date=2024-07-10"
        f"&hourly=temperature_2m&timezone=Europe%2FBerlin"
    )

    # Fetch the data from the API
    response = requests.get(url)
    data = response.json()

    # Extract hourly temperature data
    hourly = data['hourly']
    timestamps = hourly['time']
    temperatures = hourly['temperature_2m']

    # Convert to DataFrame
    df = pd.DataFrame({
        'timestamp': pd.to_datetime(timestamps),
        'temperature': temperatures
    })

    # Set timestamp as index
    df.set_index('timestamp', inplace=True)

    # Resample to daily data and calculate the daily average temperature
    daily_df = df.resample('D').mean()

    # Plotting
    plt.figure(figsize=(14, 7))
    plt.plot(daily_df.index, daily_df['temperature'], color='tab:red', label='Daily Average Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily Average Temperature from June 26, 2023 to July 10, 2024\nLocation: Athens, Greece')
    plt.legend()
    plt.grid(axis="y")
    plt.tight_layout()

    plt.show()