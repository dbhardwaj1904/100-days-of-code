import requests

STOCK_NAME = "TSLA"
STOCK_COMPANY = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "STOCK_API"
stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "5min",
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = stock_response.json()["Time Series (5min)"]
data_list = [value for (key, value) in data.items()]
last_refreshed_data = data_list[0]
last_closing_price = last_refreshed_data["4. close"]
day_before_last_day = data_list[1]
day_before_last_day_closing_price = day_before_last_day["4. close"]
difference = float(last_closing_price) - float(day_before_last_day_closing_price)
percent_diff = (difference/float(last_closing_price)) * 100

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "NEWS_API"

if percent_diff < 0:
    news_params = {
        "q": STOCK_COMPANY,
        "apikey": NEWS_API_KEY,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:1]
    message_body = [f"{STOCK_NAME}\nHeadline: {article['title']}.\nBrief description: {article['description']}"
                    for article in three_articles]
    # SEND MESSAGE AS DONE IN DAY 35
    print(message_body)
