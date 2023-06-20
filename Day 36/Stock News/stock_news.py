import os
import requests
from datetime import datetime, timedelta
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWSAPI_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


def get_stock_data(symbol, api_key):
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key,
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    return response.json()["Time Series (Daily)"]


def get_news_data(company_name, api_key):
    news_params = {
        "apiKey": api_key,
        "qInTitle": company_name,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    return news_response.json()["articles"]


def send_twilio_message(body, from_number, to_number):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=body,
        from_=from_number,
        to=to_number
    )


# Get stock data
stock_data = get_stock_data(STOCK_NAME, STOCK_API_KEY)

# Calculate dates
today = datetime.now()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

# Get closing prices for yesterday and the day before yesterday
yesterday_closing_price = float(stock_data[yesterday.strftime("%Y-%m-%d")]["4. close"])
day_before_yesterday_closing_price = float(stock_data[day_before_yesterday.strftime("%Y-%m-%d")]["4. close"])

# Calculate difference and percentage difference
difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round((difference / yesterday_closing_price) * 100)

# Get news articles if the difference percentage is greater than 5
if abs(diff_percent) > 1:
    articles = get_news_data(COMPANY_NAME, NEWS_API_KEY)
    three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. " \
                          f"\nBrief: {article['description']}" for article in three_articles]

    for article in formatted_articles:
        send_twilio_message(article, VIRTUAL_TWILIO_NUMBER, VERIFIED_NUMBER)
