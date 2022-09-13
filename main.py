import requests as requests
from twilio.rest import Client

STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "GGBF87JBCVYJYTHM"
NEWS_API = "faa5183272e944a1bb8f04169696fa4e"
TWILIO_SID = "AC0a600ce39ac22cf9c93818af6d98fe39"
TWILIO_AUTH_TOKEN = "39abe1e76eddce74a6ebd027311d7890"

## https://www.alphavantage.co/documentation/#daily


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
print(data)
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
# print(diff_percent)

up_down = None
if diff_percent > 0:
    up_down = "👆🔺↗"
else:
    up_down = "👇🔻↘"

if abs(diff_percent) > 1:
    new_params = {
        "apiKey": NEWS_API,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=new_params)
    articles = news_response.json()["articles"]


    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down} {diff_percent}% \n Headline: {article['title']}. " \
                          f"\nBrief: {article['description']}"
                          for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+16124827498",
            to="your_number"
        )

