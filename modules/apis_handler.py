import requests
from constants import API_KEY

def get_next_available(location_id):
    url = f'https://manage-livestage.solvhealth.com/partner/next-available/{location_id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]
    return None


def get_zip_code(latitude, longitude):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            for result in data['results']:
                for component in result['address_components']:
                    if 'postal_code' in component['types']:
                        return component['short_name']
    return None
