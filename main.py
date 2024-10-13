import requests
from twilio.rest import Client

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "df1c16a6f0ca8d9599929af6de140b63"
account_sid = "AC5105128009de68144e9649428a332ee6"
auth_token = "044558c04c3a55e9fe20e91e8d452f81"
weather_params = {
    "lat": 13.000328,
    "lon": 77.676468,
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
        from_="whatsapp:+14155238886",
        body="Hey Wasiiii!!\nLooks like it might rain today so you better be prepared to get drenched.☔☂️🌂",
        to="whatsapp:+919742418818"
    )

print(message.status)