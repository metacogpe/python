#
# 클래스 : 붕어빵 클, 객체나 인스턴스의 설계도 , 타입을 만들어 내는 방법
# 객체 object
# 인스턴스 

# 클래스 : 파이썬에서는 class는 meta클래스인 type클래스의 객체
# class Human: # 파이썬 내장 클래스와 달리 사용자 클래스는 대문자로 시작
#     pass
# # 

# # 
# class Human:
#     pass
# areum = Human()  # 객체가 생성되면 변수로 바인딩해서 소멸되지 않도록 해야 함 

# # 
# class Human:
#     def __init__(self): # 생성자 : 객체 생성시 자동호출
#         print('응애응애')
# areum = Human()  # 생성된 객체를 areum에 바인딩 즉, 생성자 호출

# # 
# class Human:
#     def __init__(self,name, age, sex):  # self는 객체를 받는 인자
#         self.name = name      # name이 함수 끝에서 사라지지 않도록 바인딩
#         self.age = age 
#         self.sex = sex
# areum = Human('아름',25,'여자')  # 함수 호출시 인자값 바인딩을 가장 먼저 진행
# print(areum.name)

# # 
# class Human:
#     def __init__(self,name, age, sex):  # self는 객체를 받는 인자
#         self.name = name      # name이 함수 끝에서 사라지지 않도록 바인딩
#         self.age = age 
#         self.sex = sex
#     def who(self):  # self : 메소드 사용 시 생성된 객체에서 시작(객체 바인딩)
#         print('이름: {} 나이: {} 성별: {}'.format(self.name, self.age, self.sex))
# areum = Human('아름',25,'여자')
# areum.who()   # Human.who(areum)

# #
# class Human:
#     def __init__(self,name, age, sex):  # self는 객체를 받는 인자
#         self.name = name      # name이 함수 끝에서 사라지지 않도록 바인딩
#         self.age = age 
#         self.sex = sex
    
#     def who(self):  # self : 메소드 사용 시 생성된 객체에서 시작(객체 바인딩)
#         print('이름: {} 나이: {} 성별: {}'.format(self.name, self.age, self.sex))
    
#     def setInfo(self, name, age, sex):
#         self.name = name 
#         self.age = age 
#         self.sex = sex 
    
# areum = Human('',0,'모름')
# areum.who()   # Human.who(areum)

# areum.setInfo('아름',25,'여자')  # 갱신 : 초기 임시값을 제대로 다시 셋팅
# areum.who()   # Human.who(areum)


# 
class Human:
    def __init__(self,name, age, sex):  # self는 객체를 받는 인자
        self.name = name      # name이 함수 끝에서 사라지지 않도록 바인딩
        self.age = age 
        self.sex = sex
    def __del__(self):
        print('나의 죽음을 알리지 말라')

    def who(self):  # self : 메소드 사용 시 생성된 객체에서 시작(객체 바인딩)
        print('이름: {} 나이: {} 성별: {}'.format(self.name, self.age, self.sex))
    
    def setInfo(self, name, age, sex):
        self.name = name 
        self.age = age 
        self.sex = sex 

areum = Human('아름',25,'여자')
del(areum)  # 객체 삭제 : 소멸자 호출

#
class OMG:
    def print(self): # 어떤 객체가 사용할 수 있도록 self 정의
        print('Oh my god!') 
mystock = OMG()
mystock.print()   # OMG.print(mystock)