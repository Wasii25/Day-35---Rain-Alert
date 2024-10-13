import requests
import os
from twilio.rest import Client

endpoint = "<Your openweather endpoint>"
api_key = "<Your openweather API key>"
account_sid = "<Your Twilio account SID>"
auth_token = "<Your Twilio authentication Token>"
weather_params = {
    "lat": "<Your Latitiude>",
    "lon": "<Your Longitude>",
    "appid": "<Your API key>",
    "cnt": 4,
}
response = requests.get(endpoint, params=weather_params)
weather_data = response.json()

will_rain = None

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:"+<country code><Twilio WhatsApp number>",
        body="Hey <Name>!!\nLooks like it might rain today so you better be prepared to get drenched.☔☂️🌂",
        to="whatsapp:+<Your WhatsApp Number>"
    )

print(message.status)
