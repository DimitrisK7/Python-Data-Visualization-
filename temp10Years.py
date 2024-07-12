import requests
import pandas as pd
import matplotlib.pyplot as plt


def temp10Years():
    latitude = 37.98381
    longitude = 23.727539

    def fetch_yearly_data(year):
        url = (
            f"https://archive-api.open-meteo.com/v1/archive?"
            f"latitude={latitude}&longitude={longitude}"
            f"&start_date={year}-01-01&end_date={year}-12-31"
            f"&hourly=temperature_2m&timezone=Europe%2FBerlin"
        )
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
        
        return df

    # Define the range of years
    years = range(2014, 2024)  # Adjust to the last 10 years

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

    # Resample to daily data and calculate the daily average temperature
    daily_df = df_combined.resample('D').mean()

    # Plotting
    plt.figure(figsize=(14, 7))
    plt.plot(daily_df.index, daily_df['temperature'], color='tab:red', label='Daily Average Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Daily Average Temperature for the Last 10 Years\nLocation: Athens, Greece')
    plt.legend()
    plt.grid(axis="y")
    plt.tight_layout()

    plt.show()