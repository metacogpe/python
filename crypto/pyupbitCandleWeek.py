import pyupbit
import openpyxl

df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="week")
df.to_excel("week_btc.xlsx")