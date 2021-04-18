import requests

url = "https://api.upbit.com/v1/market/all"

resp = requests.get(url)
data = resp.json()
# print(data)


krw_tickers = []
for coin in data:
    ticker = coin['market'] # coin is dict type

    if ticker.startswith("KRW"):
        krw_tickers.append(ticker)

print(krw_tickers, len(krw_tickers))

    

