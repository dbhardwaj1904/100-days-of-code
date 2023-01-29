# from twilio.rest import Client
import smtplib

TWILIO_SID = "TWILIO_SID"
AUTH_TOKEN = "TOKEN_TOKEN"
SENDER_NUMBER = "SENDER_NUMBER"
RECEIVER_NUMBER = "RECEIVER_NUMBER"


class NotificationManager:
    def __init__(self):
        pass
        # self.client = Client(TWILIO_SID, AUTH_TOKEN)

    def send_sms(self, message):
        pass
        # message = self.client.messages.create(
        #     body=message,
        #     from=SENDER_NUMBER,
        #     to=RECEIVER_NUMBER
        # )

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("SMPT ADDRESS") as connection:
            connection.starttls()
            connection.login("EMAIL", "PASSWORD")
            for email in emails:
                connection.sendmail(
                    from_addr="EMAIL",
                    to_addrs="PASSWORD",
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
