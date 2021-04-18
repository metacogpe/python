# #
# def n_plus_1(n):
#     result = n +1  # 함수가 끝나면서 result 사라짐
# n_plus_1(3)
# print(result)   # 함수 안의 변수로 이미 함수 종료시 사라짐


# 함수 내부 값을 리턴 
def make_url(name):
    domain = 'www'+name +'.com'
    return domain
result = make_url('naver') # 리턴된 값을 result가 바인딩
print(result)

# 리스트 만들기 
def make_list(mystr):
    data = []
    for i in mystr:
        data.append(i)
    return data 
a = make_list('abce')
print(a)

# 리스트의 짝수만 리턴
def pickup_even(nums):
    even = []
    for i in nums:
        if i%2 == 0:
            even.append(i)
    return even
ret = pickup_even([3,4,5,6,7,8]) # 리턴값을 받아주는 것이 필요
# 변수가 바인딩 되지 않으면 가비지 컬렉터가 회수 
print(ret)

# 컴마 포함된 숫자를 정수로 
def covert_int(mystr):
    mystr1 = mystr.replace(',','')
    return int(mystr1)
a = covert_int('1,234,567')
print(a)

#
def 함수(num):
    return num +4
a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

# 
def 함수(num):
    return num + 4
c = 함수(함수(함수(10)))
print(c)

# 