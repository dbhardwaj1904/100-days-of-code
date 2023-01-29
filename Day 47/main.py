import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.in/GeForce-192-bit-Graphics-IceStorm-ZT-A30600E-10M/dp/B08ZZW34T3/ref=sr_1_12?" \
      "crid=TY5E4NAOHH96&keywords=rtx+graphic+card+4070&qid=1674819627&sprefix=rtx+graphic+card+4070%2Caps%2C347&" \
      "sr=8-12"

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 "
                  "Safari/537.36"
}

response = requests.get(url, headers=headers)
content = response.text

soup = BeautifulSoup(content, 'lxml')
price_content = soup.findAll(name="span", class_="a-price-whole")[0]
current_price = price_content.getText().split(".")[0]
int_current_price = int(current_price.replace(",", ""))

title = soup.find(id="productTitle").getText().strip()

if int_current_price < 32000:
    SMTP_ADDR = "SMTP_ADDRESS"
    # Port number of smtp in integer
    port = 1234
    email = "User Email"
    password = "User Password"
    message = f"{title} is now {current_price}"
    body_msg = f"Subject: Amazon Price Alert!\n\n{message}\n{url}"
    with smtplib.SMTP(SMTP_ADDR, port=port) as connection:
        connection.starttls()
        result = connection.login(email, password)
        connection.sendmail(from_addr=email, to_addrs=email, msg=body_msg)