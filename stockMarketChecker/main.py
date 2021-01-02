import requests
from datetime import datetime, timedelta
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_API_KEY = 'EH6M3159XHBNNFI2'
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
News_API_Key = '5964285b697e4cf1bd5e14397e73cdd4    '

# NB: change timedeltas to 1 and 1 - no trading yesterday at point of coding due to bank holiday
yest = datetime.now() - timedelta(2)
day_before_yest = yest - timedelta(1)
yest = datetime.strftime(yest, '%Y-%m-%d')
day_before_yest = datetime.strftime(day_before_yest, '%Y-%m-%d')

stock_params = {
    'function' :'TIME_SERIES_DAILY',
    'symbol' : STOCK_NAME,
    'apikey' : stock_API_KEY,
}

response = requests.get("https://www.alphavantage.co/query", params=stock_params)

data = response.json()
yest_close = float(data['Time Series (Daily)'][yest]['4. close'])
day_before_yest_close = float(data['Time Series (Daily)'][day_before_yest]['4. close'])

change_at_close = yest_close - day_before_yest_close
percentage_difference = round(change_at_close / yest_close, 2)

stock_change = '▲' if percentage_difference > 0 else stock_change = '▼'

news_response = requests.get(f"https://newsapi.org/v2/everything?q={STOCK_NAME}&apiKey={News_API_Key}")
data = news_response.json()
news = [(article['title'], article['description']) for article in data['articles'][:4]]


account_sid ='AC272a0db926acb879fd312912f70ca74c'
auth_token = '5f19965a1357b3a7198fec1f83b995e8'

for article in news:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"{COMPANY_NAME}   {stock_change}{percentage_difference}%\nHeadline : {article[0]}\nBrief: {article[1]}\n",
        from_='+14422458253',
        to='+447875940423'
    )
    print(message.status)






