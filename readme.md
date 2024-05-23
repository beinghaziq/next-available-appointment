# Next Available Appointment
This project contains integration with Solvhealth API to get next available appointment. It takes latitude and longitude as input and uses Google API to fetch zip code.

## Features

- Integration with Solvhealth API
- Integration with google place API
- CSV data read from URL

  <img width="703" alt="Screenshot 2024-05-23 at 6 30 12 PM" src="https://github.com/beinghaziq/next-available-appointment/assets/72576839/8552ef05-a20e-435e-a735-700690ec0069">


# Build With

- Framework: Python 3.11
- FastAPI

# Getting Started

## Prerequisites

- Docker Desktop app
- python
- pip
(for new project)
- venv
```bash
  create python -m venv ./venv
  ```
- fastapi(in venv)
 ```bash
  pip install fastapi
  ```
- uvicorn(in venv)
```bash
  pip install uvicorn
  ```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/beinghaziq/next-available-appointment.git
   cd repo
   ```
2. **Install Dependencies**:
    Intall required dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup VENV(optional)**:
   - setup virtual environment
   ```bash
    source app/venv/bin/activate
   ```

4. **Run Application**:
   - Run the application
   ```bash
    uvicorn main:app --reload 
   ```
