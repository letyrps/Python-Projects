import requests
from twilio.rest import Client

parameters = {
   'latitude': -27.758294,
   'longitude': 48.632759,
   'current_weather': True
}
resposnce = requests.get(url='https://api.open-meteo.com/v1/forecast', params=parameters)
resposnce.raise_for_status()
data = resposnce.json()
temperature = data['current_weather']['temperature']
def check_weather():
   if temperature <= 10:
      return f'Sleep day, Temp: {temperature}'
   elif 11 <= temperature < 20:
      return f'Bring a colt, Temp: {temperature}'
   elif 21 <= temperature < 25:
      return f'Perfect weather, Temp: {temperature}'
   elif 25 <= temperature < 30:
      return f'Use sunscreen, Temp: {temperature}'
   elif temperature >= 30:
      return f'Go to the beach, Temp: {temperature}'

text = check_weather()

account_sid = 'ACe0b738fb2577d6be1467a261351dae79'
auth_token = 'b2baf7f96f8cbad2683d037d1a5c64c0'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+16813846904',
  body=f'{text}',
  to='+5548991570913'
)
print(message.status)