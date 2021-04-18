# 역순 출력
def print_reverse(mystr):
    print(mystr[::-1])
print_reverse('hello')

# 성적 평균
def print_score(scores):  # python list
    averge = sum(scores)/len(scores)
    print(averge)
print_score([1,2,3])

# 하나의 리스트 입력 받아 짝수만 출력
def print_even(data):
    for i in data: 
        if i%2 ==0:
            print(i)
print_even([1,2,3,4])

# 하나의 딕셔너리의 키 값 출력
def print_keys(mydict):
    keys = mydict.keys()
    for k in keys: 
        print(k)
print_keys({'이름':'홍길동','나이':20})

# 딕셔너리와 키값으로 호출
my_dict = { '10/26':[100,130,100,100],
            '10/27':[10,12,10,11]}
def print_value_by_key(mydict, key):
    print(mydict[key])
print_value_by_key(my_dict, '10/27')

# 5글자까지 자르기
def print_5xn(mystr):
    times = len(mystr)/5
    times = int(times+0.9)
    for i in range(times):
        print(mystr[5*i:5*i+5])
print_5xn("아이엠어보이유알어걸1")


# 숫자만큼 끊어서 출력
import math
a = math.ceil(2.1) #올림
print(a)

def printmxn(data, num):
    times = len(data)/num
    times = math.ceil(times)

    for i in range(times):
        print(data[i*num: (i+1)*num])
printmxn("아이엠어보이유알어걸1",3)

# 월급 연봉
def calc_month_salary(annual):
    print(int(annual/12))
calc_month_salary(12000000)

# 명시적 인자 호출
def my_print(a,b):
    print('왼쪽:', a)
    print('오른쪽:', b)
my_print(a=100, b=200)


