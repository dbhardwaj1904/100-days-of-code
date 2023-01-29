import requests
from datetime import datetime

TRACK_NUTRITIONIX_API = "https://trackapi.nutritionix.com"
exercise_endpoint = TRACK_NUTRITIONIX_API + "/v2/natural/exercise"
app_id = "APP_ID"
api_key = "APP_KEY"

input_exercise = input("Which exercises you did: ")
gender = "MALE"
weight = "54"
height = "164"
age = "24"

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}
params = {
    "query": input_exercise,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}
response = requests.post(exercise_endpoint, json=params, headers=headers)

exercises = response.json()["exercises"]
google_sheets_api = "GOOGLE_SHEETS_API"
for exercise in exercises:
    auth = (
        "YOUR_USERNAME",
        "YOUR_PASSWORD",
    )
    params = {
        "workout": {
            "date": (datetime.now()).strftime("%d/%m/%Y"),
            "time": (datetime.now()).strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(google_sheets_api, json=params, auth=auth)
    print(response.json())
