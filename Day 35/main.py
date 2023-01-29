import requests
# from twilio.rest import Client

# Weather Details
API_KEY = "WEATHER_API"
LAT = 30.9084
LONG = 77.0999
URL = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
}
response = requests.get(URL, params=params)
w_id = response.json()["weather"][0]["id"]
w_main = response.json()["weather"][0]["main"]
w_description = response.json()["weather"][0]["description"]


# TWILIO
account_sid = "ACCOUNT_ID"
auth_token = "AUTH_TOKEN"
message_body = "Hello, User!"
sender_ph = "SENDER_PHONE_NUMBER"
receiver_ph = "RECEIVER_PHONE_NUMBER"
# client = Client(account_sid, auth_token)
# message = client.messages.create(body=message_body,from=sender_ph,to=receiver_ph)
