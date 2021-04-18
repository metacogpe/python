#함수 : 자주 사용 코드를 함수를 메모리에 로딩
#함수의 이름이 코드를 바인딩한다.
def print_coin():    
    print('비트코인')
print_coin() # 함수로 정의된 코드를 실행하라.

for i in range(100): # 100번 반복 호출
    print_coin()

# 100번 호출을 함수로 생성
def print_coins():
    for i in range(100): # 100번 반복 호출
        print('비트코인')

# 에러 발생 사유 확인 : 함수의 이름은 코드를 바인딩
# hello()   # hello()가 정의되어 있지 않아 바인딩 없음
# def hello():
#     print('Hi')

#
def message():
    print('A')
    print('B')
message()
print('c')
message()

# 
def message1():
    print('A')

def message2():
    print('B')
    message1()
message2()



# 
def message1():
    print('A')
def message2():
    print('B')
def message3():
    for i in range(3):
        message2()
        print('C')
    message1()
message3()
