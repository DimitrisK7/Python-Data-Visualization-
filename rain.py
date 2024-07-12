import requests
import pandas as pd
import matplotlib.pyplot as plt

def rain():
    latitude = 37.98381
    longitude = 23.727539
    years = range(2014, 2024)  # Last 10 years

    # Define the URL for the API request including rainfall data
    def fetch_yearly_data(year):
        url = (
            f"https://archive-api.open-meteo.com/v1/archive?"
            f"latitude={latitude}&longitude={longitude}"
            f"&start_date={year}-01-01&end_date={year}-12-31"
            f"&hourly=rain&timezone=Europe%2FBerlin"
        )
        response = requests.get(url)
        data = response.json()
        
        # Extract hourly rain data
        hourly = data['hourly']
        timestamps = hourly['time']
        rain = hourly['rain']
        
         # Convert to DataFrame
        df = pd.DataFrame({
            'timestamp': pd.to_datetime(timestamps),
            'rain': rain
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
    plt.bar(daily_df.index, daily_df['rain'], color='tab:blue', width=1.0, label='Daily Average Rain')
    plt.xlabel('Date')
    plt.ylabel('rain (mm)')
    plt.title('Daily rain for the last 10 years\nLocation: Athens, Greece')
    plt.legend()
    plt.grid(axis="y")
    plt.tight_layout()
    
    plt.show()