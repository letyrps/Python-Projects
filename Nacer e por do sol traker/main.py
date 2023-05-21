import requests
MY_LAT = -27.758261
MY_LONG = -48.632743
from datetime import datetime

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
# print(data)
parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}
resposnce = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
resposnce.raise_for_status()
data = resposnce.json()
sunrise = data['results']['sunset'].split('T')[1].split(':')[0]
sunset = data['results']['sunrise'].split('T')[1].split(':')[0]
time_now = datetime.now()
print(time_now.hour)