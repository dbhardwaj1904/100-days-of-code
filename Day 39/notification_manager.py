# from twilio.rest import Client

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
