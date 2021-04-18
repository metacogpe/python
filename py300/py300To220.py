# 호출결과 예상
def 함수(문자열):  #  함수 호출 시 인자값 바인딩
    print(문자열)
함수('안녕')
함수('Hi')

# 함수 인자 다수 받기
def func(a,b):
    print(a+b)
func(3,4)

# 함수 인자 받기와 타입

# 함수 정의 
def print_with_smile(mystr):
    print(mystr + ':D')

# 
print_with_smile('안녕하세요')

# 
def print_upper_price(price):
    상한가 = price * 1.3
    print(상한가)
print_upper_price(10000)
print_upper_price(20000)

# 4칙 연산
def print_arith_oper(a,b):
    a = 3
    b =4 
    print("{} +{} = {}".format(a, b, a+b))
    print("{} -{} = {}".format(a, b, a-b))
    print("{} *{} = {}".format(a, b, a*b))
    print("{} /{} = {}".format(a, b, a/b))
print_arith_oper(3,5)

# 
def print_max(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>c and b>a:
        print(b)
    else:
        print(c)

print_max(10,1,2)
print_max(10,20,2)
print_max(10,20,30)

