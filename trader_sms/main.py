STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
from twilio.rest import Client

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
api_key_alfa = 'ES23NFBY1XKZ1RCP'
parameters = {
   'function': 'TIME_SERIES_INTRADAY',
   'symbol': 'TSLA',
   'interval': '60min',
   'outputsize': 'full',
   'apikey': 'ES23NFBY1XKZ1RCP'
}
resposnce = requests.get(url='https://www.alphavantage.co/query?', params=parameters)
resposnce.raise_for_status()
data = resposnce.json()

#taking data from 2 days ago
two_days_past_date = data['Meta Data']["3. Last Refreshed"]
two_days_past_day = two_days_past_date.split()[0]
two_days_past_day_16 = f'{two_days_past_day} 16:00:00'

#taking data from 3 days ago
three_days_past = list(data["Time Series (60min)"])
three_days_past_day = three_days_past[16].split()[0]
three_days_past_day = f'{three_days_past_day} 16:00:00'

#printing_data
two_days_past_data = data["Time Series (60min)"][f'{two_days_past_day_16}']
three_days_past_data = data["Time Series (60min)"][f'{three_days_past_day}']


#taking close value of these two days
close_three_days_past = float(three_days_past_data['4. close'])
close_two_days_past = float(two_days_past_data['4. close'])
diference = close_three_days_past - close_two_days_past
diference = round(diference, 2)

percent = round((100*diference)/close_three_days_past, 2)

#using api news to take data
api_key_news = '820dd592abce4b0696abcc3ee0c3eb96'
parameters = {
   'q': 'tsla',
   'sortBy': 'Date published',
   'apikey': api_key_news
}
resposnce = requests.get(url='https://newsapi.org/v2/everything?', params=parameters)
resposnce.raise_for_status()
data_news = resposnce.json()
articles = data_news["articles"][0:3]

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

def get_news():
   title = articles[0]['title']
   descripition = articles[0]['description']
   return f'Headline: {title}\nBrief: {descripition}'

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

def send_sms(p_text):
   account_sid = 'ACe0b738fb2577d6be1467a261351dae79'
   auth_token = 'b2baf7f96f8cbad2683d037d1a5c64c0'
   client = Client(account_sid, auth_token)

   message = client.messages.create(
      from_='+16813846904',
      body=f'{p_text}',
      to='+5548991570913'

   )
   print(message.status)

if percent <= -5:
   text_ = get_news()
   text = f'TESLA: 🔻{percent}\n{text_}'
   send_sms(text)
elif percent >= 5:
   text_ = get_news()
   text = f'TESLA: 🔺{percent}\n{text_}'
   send_sms(text)
elif -5 < percent < 5:
   text_ = get_news()
   text = f'No change for TSLA\nTESLA: {percent}\n{text_}'
   send_sms(text)




#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

