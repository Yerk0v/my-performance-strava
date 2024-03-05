import requests
import csv

API_KEY = 'GhAgmfHGrXw4ExMdjVYs6EhVLPzOIf9Q'
LOCATION_KEY = '57535'  # Replace with the location key for Menque
START_DATE = '2024-03-01'
END_DATE = '2024-03-05'

url = f'https://dataservice.accuweather.com/currentconditions/v1/{LOCATION_KEY}/historical/24?apikey={API_KEY}&details=true&startdate={START_DATE}&enddate={END_DATE}'
response = requests.get(url)
data = response.json()

# Specify the fields you want to include in the CSV file
fields = data[0].keys()

# Specify the name of the CSV file
csv_file = 'historical_weather_data.csv'

# Write data to CSV file
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

print(f"Data has been saved to {csv_file}.")


