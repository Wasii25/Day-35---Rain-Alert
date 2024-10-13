import requests
import os
from twilio.rest import Client

endpoint = os.environ["endpoint"]
api_key = os.environ["api_key"]
account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]
weather_params = {
    "lat": None,
    "lon": None,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(endpoint, params=weather_params)
weather_data = response.json()

# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = None

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+Twilio Whatsapp number",
        body="Hey <NAME>!!\nLooks like it might rain today so you better be prepared to get drenched.☔☂️🌂",
        to="whatsapp:+<YOUR WHATSAPP NUMBER>"
    )

print(message.status)