for i in range(0,100):
    print(i)

for i in range(2002, 2050+1, 4):
    print(i)

for i in range(3,30,3):
    print(i)

for i in range(99, -1, -1):
    print(i)

for i in range(0,10):
    print('0.', i)


for i in range(1,10):
    print('3 X', i, '=', 3*i)

for i in range(1,10, 2):
    print('3 X', i, '=', 3*i)


result =0
for i in range(1,11):
    result = result + i # result + = i
print('합:', result)

result = 0
for i in range(1,10,2):
    result += i
print("합: ", result)

result = 1 # 곱셈 초기값
for i in range(1,11):
    result = result * i 
print('누적곱:', result)
    