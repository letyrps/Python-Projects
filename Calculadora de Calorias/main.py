import requests
import datetime as dt
import requests

APP_ID = '4fac52ba'
API_KEY = 'b37788b8e07c5fb755ad351614d236c6'
DATE = dt.datetime
today = DATE.today().date()
today_date = str(today).replace('-', '/')
today_time = str(DATE.today().time().fromisoformat('04:23:01'))



GENDER = "MALE"
WEIGHT_KG = "60"
HEIGHT = "160.5"
AGE = "50"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    'query': exercise_input
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
print(result)

sheety_end_point  ='https://api.sheety.co/f6112874538f446e8e05328d725b6a85/myWorkouts/workouts'

header = {"Content-Type": "application/json"}

params_sheety = {
   'workouts': {
      'date': today_date,
      'time': today_time,
       'exercise': result['exercises'][0]['user_input'],
      'duration': result['exercises'][0]["duration_min"],
      'calories': result['exercises'][0]["nf_calories"]
   }
}

sheet_response = requests.post(sheety_end_point, json=params_sheety)

result_sheety = response.text
print(result_sheety)