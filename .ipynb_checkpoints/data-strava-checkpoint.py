import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "122287",
    'client_secret': '465cfaf8626df981f0ee4b8bccf5bb23e4f124cd',
    'refresh_token': '2463705053e80ed434389ac424fbffaa3c306f92',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}

total_activities = 10
per_page = 200
page_number = (total_activities - 1) // per_page + 1

param = {'per_page': per_page, 'page': page_number}
my_dataset = requests.get(activites_url, headers=header, params=param).json()


if my_dataset:
    relevant_variables = ['athlete', 'name', 'distance', 'moving_time', 'elapsed_time', 'total_elevation_gain', 'type', 'sport_type', 'workout_type', 'id', 'start_date', 'start_date_local', 'timezone']
    relevant_activities = [{variable: activity[variable] for variable in relevant_variables} for activity in my_dataset]
    for activity in relevant_activities:
        print(activity)
else:
    print("No activities found")

import csv

# Define the file name for the CSV file
csv_file = 'relevant_activities.csv'

# Check if there are any activities
if my_dataset:
    # Define the variables you want to keep
    relevant_variables = ['athlete', 'name', 'distance', 'moving_time', 'elapsed_time', 'total_elevation_gain', 'type', 'sport_type', 'workout_type', 'id', 'start_date', 'start_date_local', 'timezone']
    
    # Create a list of dictionaries, each representing a row with relevant variables
    relevant_activities = [{variable: activity[variable] for variable in relevant_variables} for activity in my_dataset]
    
    # Write the relevant activities to a CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=relevant_variables)
        writer.writeheader()
        for activity in relevant_activities:
            writer.writerow(activity)
    print(f"CSV file '{csv_file}' saved successfully.")
else:
    print("No activities found")
