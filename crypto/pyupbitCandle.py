import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC", "minute1")
print(df)

df = pyupbit.get_ohlcv("KRW-BTC", "minute3")
print(df)


df['open'].resample('3T').first()  # 3개 단위(여기서는 3분) 리샘플

print(df)