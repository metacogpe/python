# 일별 가격 
data = [
    [2000,3050,2050,1980],
    [7500,2050,2050,1980],
    [15450,15050,15550,14900]
]

for day in data:
    for price in day:
        print(price +(price * 0.014 * 0.01))


#
data = [
    [2000,3050,2050,1980],
    [7500,2050,2050,1980],
    [15450,15050,15550,14900]
]

for day in data:
    for price in day:
        print(price +(price * 0.014 * 0.01))
    print('-'*4)


# 
data = [
    [2000,3050,2050,1980],
    [7500,2050,2050,1980],
    [15450,15050,15550,14900]
]

result = []
for day in data:
    for price in day:
        result.append(price +(price * 0.014 * 0.01))

print(result)


# 
data = [
    [2000,3050,2050,1980],
    [7500,2050,2050,1980],
    [15450,15050,15550,14900]
]

result = []
for day in data:
    day_price = []
    
    for price in day:
        new_price = price +(price * 0.014 * 0.01)
        day_price.append(new_price)
    result.append(day_price)
print(result)


# 
ohlc = [ ['open','high','low','close'],
         [100,110,70,100],
         [200,210,180,190],
         [300,310,300,310]
]

for day_price in ohlc[1:]:
    close = day_price[3]
    if close >150:
        print(close)


# 
ohlc = [ ['open','high','low','close'],
         [100,110,70,100],
         [200,210,180,190],
         [300,310,300,310]
]

for day_price in ohlc[1:]:
    open = day_price[0]
    close = day_price[3]
    if close >= open:
        print(close)


# 변동폭 : 고가 - 저가 
# volatitlity = []
ohlc = [ ['open','high','low','close'],
         [100,110,70,100],
         [200,210,180,190],
         [300,310,300,310]
]

volatility = []
for day_price in ohlc[1:]:
    high = day_price[1]
    low = day_price[2]
    diff = high - low
    volatility.append(diff)
print(volatility)


# 종가>시가, 변동(고가-저가)
ohlc = [ ['open','high','low','close'],
         [100,110,70,100],
         [200,210,180,190],
         [300,310,300,310]
]
for day_price in ohlc[1:]:
    open, high, low, close = day_price #언패킹
    if close > open:
        print(high-low)


# 수익금: 시가 -종가 
# 총수익금

ohlc = [ ['open','high','low','close'],
         [100,110,70,100],
         [200,210,180,190],
         [300,310,300,310]
]
total_profit = 0
for day_price in ohlc[1:]:
    profit = day_price[0] - day_price[3]
    total_profit += profit
print(total_profit)
