#
import random
num = random.randint(0,99)
print(num)
str(num).zfill(5)# 00099 zerofill 메소스 

class Account:
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        self.account_number = num1 + '-'+num2 +'-'+ num3

kim = Account("김민수",100)
print(kim.name)
print(kim.balance)
print(kim.bank)
print(kim.account_number)

# 클래스 변수 : 클래스 공간에 저장되는 변수 
# 클래스 공간, 객체공간 a, 객체공간 b
# 객체에 저장되는 변수 : instance variable 
# 각각의 객체가 고유의 정보 관리 
# 클래스 변수 : 각 객체가 참조 필요 없는 정보
#  

class Account:
    account_count = 0  # 클래스 변수 : 객체가 참조 불필요 
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        self.account_number = num1 + '-'+num2 +'-'+ num3
        Account.account_count +=1 # 계좌 개설 시 증가
kim = Account("김민수",100)  
print(Account.account_count)      
    
lee = Account("이민수",100)  
print(Account.account_count) # 계좌의 갯수 출력 가능

# 

class Account:
    account_count = 0  # 클래스 변수 : 객체가 참조 불필요 
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        self.account_number = num1 + '-'+num2 +'-'+ num3
        Account.account_count +=1 # 계좌 개설 시 증가
        
    @classmethod  # 객체를 참조할 필요가 없는 메소드
    def get_account_num(cls): # self 대신에 cls 사용 
        print(cls.account_count)

    def deposit(self, amount):  # 입금 
        if amount >=1:
            self.balance += amount  # 잔고에 추가 


kim = Account("김민수",100)  
lee = Account("이민수",100)  
kim.get_account_num() # Account.get_account_num(kim)


#
import random
class Account:
    account_count = 0  # 클래스 변수 : 객체가 참조 불필요 
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        self.account_number = num1 + '-'+num2 +'-'+ num3
        Account.account_count +=1 # 계좌 개설 시 증가
        
    @classmethod  # 객체를 참조할 필요가 없는 메소드
    def get_account_num(cls): # self 대신에 cls 사용 
        print(cls.account_count)

    def deposit(self, amount):  # 입금 
        if amount >=1:
            self.balance += amount  # 잔고에 추가
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

k= Account("kim",180)
k.withdraw(90)
print(k.balance)

# 정보 출력 메소드 
import random
class Account:
    account_count = 0  # 클래스 변수 : 객체가 참조 불필요 
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        self.account_number = num1 + '-'+num2 +'-'+ num3
        Account.account_count +=1 # 계좌 개설 시 증가
        
    @classmethod  # 객체를 참조할 필요가 없는 메소드
    def get_account_num(cls): # self 대신에 cls 사용 
        print(cls.account_count)

    def deposit(self, amount):  # 입금 
        if amount >=1:
            self.balance += amount  # 잔고에 추가
    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

p = Account("파이썬", 10000)
p.display_info()

# 이자 지급하는 코드 
import random
class Account:
    account_count = 0  # 클래스 변수 : 객체가 참조 불필요 
    def __init__(self, name, balance):
        self.deposit_count = 0
        self.name = name 
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        self.account_number = num1 + '-'+num2 +'-'+ num3
        Account.account_count +=1 # 계좌 개설 시 증가
        
    @classmethod  # 객체를 참조할 필요가 없는 메소드
    def get_account_num(cls): # self 대신에 cls 사용 
        print(cls.account_count)

    def deposit(self, amount):  # 입금 
        if amount >=1:
            self.balance += amount  # 잔고에 추가

            self.deposit_count += 1 # deposit 시 카운트 추가 
            if self.deposit_count %5 == 0:
                #이자지급
                self.balance = (self.balance * 1.01)

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)
p = Account("파이썬",10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(5000)
p.deposit(5000)
print(p.balance)


# 278
import random
class Account:
    account_count = 0  # 클래스 변수 : 객체가 참조 불필요 
    def __init__(self, name, balance):
        self.deposit_count = 0
        self.name = name 
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        self.account_number = num1 + '-'+num2 +'-'+ num3
        Account.account_count +=1 # 계좌 개설 시 증가
        
    @classmethod  # 객체를 참조할 필요가 없는 메소드
    def get_account_num(cls): # self 대신에 cls 사용 
        print(cls.account_count)

    def deposit(self, amount):  # 입금 
        if amount >=1:
            self.balance += amount  # 잔고에 추가

            self.deposit_count += 1 # deposit 시 카운트 추가 
            if self.deposit_count %5 == 0:
                #이자지급
                self.balance = (self.balance * 1.01)

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

data = []
k = Account("kim", 10000000)
l = Account("lee", 10000)
p = Account("park", 10000)

data.append(k)
data.append(l)
data.append(p)
# print(data)

for c in data:
    if c.balance >= 1000000:
        c.display_info()  # 279번 예제

# 
# 280
import random
class Account:
    account_count = 0  # 클래스 변수 : 객체가 참조 불필요 
    
    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = [] # 입금 이력용
        self.withdraw_log = [] # 출금 이력용
        self.name = name 
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(3)
        num3 = str(num3).zfill(3)

        self.account_number = num1 + '-'+num2 +'-'+ num3
        Account.account_count +=1 # 계좌 개설 시 증가
        
    @classmethod  # 객체를 참조할 필요가 없는 메소드
    def get_account_num(cls): # self 대신에 cls 사용 
        print(cls.account_count)

    def deposit(self, amount):  # 입금 
        if amount >=1:
            self.deposit_log.append(amount)
            self.balance += amount  # 잔고에 추가

            self.deposit_count += 1 # deposit 시 카운트 추가 
            if self.deposit_count %5 == 0:
                #이자지급
                self.balance = (self.balance * 1.01)
    def withdraw(self, amount):
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)

k = Account("kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw(300)
k.withdraw_history()
