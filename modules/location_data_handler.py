from fastapi import HTTPException
import requests
import csv
from constants import CSV_URL

def load_location_data():
    response = requests.get(CSV_URL)
    if response.status_code == 200:
        csv_data = response.text.splitlines()
        reader = csv.DictReader(csv_data)
        location_data = {row['location_id']: row['zip_code'] for row in reader}
        return location_data
    else:
        raise HTTPException(status_code=response.status_code,
                            detail="Failed to fetch location data from the URL")
