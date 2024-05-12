import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YPZY6EPEFIRX25SJ"
NEWS_API_KEY = "d48f7daa217e463b8ad8dec7cfebec07"

TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

stock_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    # "interval": "1min",
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameter)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_data_closing_price))

percentage_diff = (difference / float(yesterday_closing_price)) * 100

if percentage_diff > 1:
    news_params = {
        "apiKey": "d48f7daa217e463b8ad8dec7cfebec07",
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+55555555",
            to="+880000000"
        )




