from fastapi import FastAPI
from controllers.next_available_appointment_controller import router

app = FastAPI()


app.include_router(router, prefix='/next-available-appointment',
                   tags=['next-available-appointment'])
