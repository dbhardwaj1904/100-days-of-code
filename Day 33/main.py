from datetime import datetime
import requests
import smtplib
import time

LAT = 30.9084
LONG = 77.0999
my_email = "sender_mail_id"
receiver_email = "sample.mail@gmail.com"
password = "app_password"
email_header = "Subject: Look up"
email_body = "ISS is above you in sky."

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

latitude = float(data["iss_position"]["latitude"])
longitude = float(data["iss_position"]["longitude"])


def is_iss_overhead():
    if (LAT - 5) <= latitude <= (LAT + 5) and (LONG - 5) <= longitude <= (LONG + 5):
        return True


def is_night():
    parameters = {
        "lat": LAT,
        "long": LONG,
        "formatted": 0,
    }

    response1 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response1.raise_for_status()
    data1 = response1.json()
    sunrise = int(data1["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data1["results"]["sunset"].split("T")[1].split(":")[0])
    current_time = datetime.now().hour
    if current_time >= sunset or current_time <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=receiver_email,
                msg=f"{email_header}\n\n{email_body}"
            )
