# 
class Stock:
    def __init__(self, name, code):
        self.name = name 
        self.code = code 
삼성 = Stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)


#
class Stock:
    def __init__(self, name, code):
        self.name = name 
        self.code = code 
    
    def set_name(self, name):  # 여러 객체별 설정을 위한 메소드로 self 인자 사용
        self.name = name
a = Stock(None, None)
a.set_name("삼성전자")
print(a.name)  

#
class Stock:
    def __init__(self, name, code):
        self.name = name 
        self.code = code 
    
    def set_name(self, name):  # 여러 객체별 설정을 위한 메소드로 self 인자 사용
        self.name = name
    
    def set_code(self, code):  # 여러 객체별 설정을 위한 메소드로 self 인자 사용
        self.code = code
a = Stock(None, None)
a.set_code("005930")
print(a.code)  

#
class Stock:
    def __init__(self, name, code):
        self.name = name 
        self.code = code 
    
    def set_name(self, name):  # 여러 객체별 설정을 위한 메소드로 self 인자 사용
        self.name = name
    
    def set_code(self, code):  # 여러 객체별 설정을 위한 메소드로 self 인자 사용
        if len(code) != 6:
            print("오류코드")
        self.code = code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    
삼성 = Stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)  

print(삼성.get_name())
print(삼성.get_code())  

#
class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name 
        self.code = code 
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률
    
    def set_name(self, name):  # 여러 객체별 설정을 위한 메소드로 self 인자 사용
        self.name = name
    def set_code(self, code):
        self.code = code 
    
    def get_name(self):
        return self.name
        return self.code 
    

# 
삼성 = Stock("삼성전자","005930", 15.79, 1.33, 2.83)
print(삼성.배당수익률)

# 
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name 
        self.code = code 
        self.per = per
        self.pbr = pbr
        self.dividend = dividend
    
    def set_name(self, name):  # 여러 객체별 설정을 위한 메소드로 self 인자 사용
        self.name = name
    def set_code(self, code):
        self.code = code 
    
    def set_per(self, per):
        self.per = per 
    
    def set_pbr(self, pbr):
        self.pbr = pbr 

    def set_dividend(self, dividend):
        self.dividend = dividend 


# set_per
종목 = []
삼성 = Stock("삼성전자","005930", 15.79, 1.33,2.82)
삼성.set_per(12.75)
print(삼성.per)

# 개체 3개 생성 후 리스트에 저장 
삼성 = Stock("삼성전자","005930", 15.79, 1.33,2.82)
현대차 = Stock("현대차","005480", 8.79, 0.35, 4.27)
LG전자 = Stock("LG전자","066570", 317.34, 0.49,1.37)
종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)
