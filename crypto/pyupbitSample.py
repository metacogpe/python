import pyupbit # python -m pip install pyupbit

tickers = pyupbit.get_tickers()
print(tickers)
print(len(tickers))

tickers = pyupbit.get_tickers(fiat="KRW")
print(tickers)

tickers = pyupbit.get_tickers(fiat="BTC")
print(len(tickers))