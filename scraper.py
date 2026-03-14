import requests
import pandas as pd
import datetime
import os

# API endpoints for Toronto Bike Share
status_url = 'https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_status'
info_url = 'https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_information'

# Pull the live data
status_data = requests.get(status_url).json()['data']['stations']
info_data = requests.get(info_url).json()['data']['stations']

# Merge the dataframes
df_status = pd.DataFrame(status_data)
df_info = pd.DataFrame(info_data)
df = pd.merge(df_status, df_info, on='station_id')

# Filter for the Beach BIA bounding box
beach_stations = df[
    (df['lon'] >= -79.315) & (df['lon'] <= -79.280) &
    (df['lat'] >= 43.660) & (df['lat'] <= 43.675)
].copy()


# Select useful columns and add a timestamp
beach_stations = beach_stations[['name', 'num_bikes_available', 'num_docks_available']]
beach_stations['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Save or append to the CSV
csv_filename = 'beach_bike_data.csv'
if not os.path.isfile(csv_filename):
    beach_stations.to_csv(csv_filename, index=False)
else:
    beach_stations.to_csv(csv_filename, mode='a', header=False, index=False)