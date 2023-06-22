import requests
from datetime import datetime
import os
from requests.auth import HTTPBasicAuth

# Your personal data. Used by Nutritionix to calculate calories.
GENDER = "male"
WEIGHT_KG = 88
HEIGHT_CM = 192
AGE = 24

# Nutritionix APP ID and API Key. Actual values are stored as environment variables.
APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Prompt the user for exercise input
exercise_text = input("Tell me which exercises you did: ")

# Nutritionix API Call
headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}
parameters = {"query": exercise_text, "gender": GENDER, "weight_kg": WEIGHT_KG, "height_cm": HEIGHT_CM, "age": AGE}

result = None  # Assigning a default value to result

try:
    response = requests.post(exercise_endpoint, json=parameters, headers=headers)
    response.raise_for_status()
    result = response.json()
    print(f"Nutritionix API call: \n {result} \n")
except requests.exceptions.RequestException as e:
    print(f"Error during Nutritionix API call: {e}")

# Adding date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety Project API. Check your Google sheet name and Sheety endpoint
GOOGLE_SHEET_NAME = "workout"
sheet_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]
username = os.environ["ENV_SHEETY_USERNAME"]
password = os.environ["ENV_SHEETY_PASSWORD"]

# Sheety API Call & Authentication
for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {"date": today_date, "time": now_time, "exercise": exercise["name"].title(), "duration": exercise["duration_min"], "calories": exercise["nf_calories"]}}

    try:
        sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=HTTPBasicAuth(username, password))
        sheet_response.raise_for_status()
        print(f"Sheety Response: \n {sheet_response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error during Sheety API call: {e}")
