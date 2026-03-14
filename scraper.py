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

# List of specific station IDs provided by you
target_ids = ["7319", "7313", "7309", "7303", "8190", "7314", "7427", "7695", "7428", "7365", "7692", "7315", "7317", "7318", "7316", "7364"]

# Filter the dataframe to only include these IDs
# This converts everything to a string before checking, so it never fails
beach_stations = df[df['station_id'].astype(str).isin(target_ids)].copy()

# Select useful columns and add a timestamp
beach_stations = beach_stations[['station_id', 'name', 'lat', 'lon', 'capacity', 'num_bikes_available', 'num_docks_available']]
beach_stations['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Save or append to the CSV
csv_filename = 'beach_bike_data.csv'
if not os.path.isfile(csv_filename):
    beach_stations.to_csv(csv_filename, index=False)
else:
    beach_stations.to_csv(csv_filename, mode='a', header=False, index=False)