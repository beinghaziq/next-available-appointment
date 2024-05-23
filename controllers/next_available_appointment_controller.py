from fastapi import APIRouter, HTTPException, Query
from modules.apis_handler import get_zip_code, get_next_available
from modules.location_data_handler import load_location_data

router = APIRouter()

@router.get('')
def next_available_appointment(latitude: float = Query(..., description="Latitude of the location"),
                               longitude: float = Query(..., description="Longitude of the location")):
    zip_code = get_zip_code(latitude, longitude)
    if not zip_code:
        raise HTTPException(
            status_code=400, detail="Failed to retrieve zip code from provided latitude and longitude.")
    location_data = load_location_data()
    relevant_locations = [location_id for location_id,
                          loc_zip in location_data.items() if loc_zip == zip_code]

    if not relevant_locations:
        raise HTTPException(
            status_code=404, detail="No clinic locations found in the provided zip code.")
    appointments = []
    for location_id in relevant_locations:
        appointment = get_next_available(location_id)
        if appointment:
            appointments.append(appointment)

    if not appointments:
        raise HTTPException(
            status_code=404, detail="No available appointments found in the provided zip code.")

    soonest_appointment = min(
        appointments, key=lambda x: x['epoch_time'])
    return soonest_appointment
