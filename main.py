import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

APP_ID = "f9d9d9f6"
API_KEY = "05e84f5beb0d1a9b74776d40e342b5ea"
sheetly_user_name = "c8c4c0505bc3dd179735cf20b98e4c61"
sheetly_proj_name = "workoutTracking"
sheetly_sheet_name = "workouts"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

domain_url = "https://trackapi.nutritionix.com"
url_endpoint = "/v2/natural/exercise"
request_url = domain_url + url_endpoint

sheetly_url = f"https://api.sheety.co/{sheetly_user_name}/{sheetly_proj_name}/{sheetly_sheet_name}"


def get_exercise():
    exercise_input = input("Please Enter Exercises you did today : ")

    body = {
        "query": exercise_input
    }

    response = requests.post(url=request_url, json=body, headers=headers)
    response.raise_for_status()
    return response.json()


def post_stats():
    basic = HTTPBasicAuth('user', 'pass')

    data = get_exercise()
    for exercise in data['exercises']:
        sheet_input = {
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": exercise['user_input'].title(),
                "duration": exercise['duration_min'],
                "calories": exercise['nf_calories'],
            }
        }

        res = requests.post(url=sheetly_url, json=sheet_input, auth=basic)
        res.raise_for_status()


post_stats()
# user_inp = input("Do you want add workout Y/N : ")
# while user_inp.lower() != 'n':
#     post_stats()
#     user_inp = input("Do you want to add more exercise Y/N : ")
