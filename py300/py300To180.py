price_list = [32100,32150,32000,32500]
for i in range(0,4):
    print(price_list[i])

price_list = [32100,32150,32000,32500]
for i in range(0,4):
    print(i, price_list[i])

price_list = [32100,32150,32000,32500]
for i in range(0,4):
    print(3-i, price_list[i])

price_list = [32100,32150,32000,32500]
for i in range(1,4):
    print(i*10+90, price_list[i])


my_list = ['가','나','다', '라']
for i in range(0,3):
    print(my_list[i], my_list[i+1])

my_list = ['가','나','다', '라', '마']
for i in range(0,3):
    print(my_list[i], my_list[i+1], my_list[i+2])

my_list = ['가','나','다', '라']
for i in range(3,0,-1):
    print(my_list[i], my_list[i-1])


my_list = [100,200,400,800]
for i in range(0,3):
    print(my_list[i+1] - my_list[i])

#이동평균
my_list = [100,200,400,800,1000,1300]
for i in range(0,4):
    hap = my_list[i] + my_list[i+1] + my_list[i+2]
    print(hap/3)

# 변동폭
low_prices = [100,200,400,800,1000]
high_prices = [150,300,430,880,1000]
volatility = []
for i in range(5):
    diff = high_prices[i] - low_prices[i]
    volatility.append(diff)
print(volatility)



