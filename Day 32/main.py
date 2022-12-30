# Create App password for sending email in sender account
# For example in gmail - Manage Account > Security > Two-Step verification
# After Two-Step > App passwords

import pandas
import smtplib
from datetime import datetime as dt

today = (dt.now().month, dt.now().day)

my_email = "sender_mail_id"
password = "app_password"

email_header = "Subject: Hello"
email_body = "You are a SIGMA person"

file = pandas.read_csv("quotes.csv")
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in file.iterrows()}

if today in birthday_dict:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="another_sample.mail@gmail.com",
            msg=f"{email_header}\n\n{email_body}"
        )
