# 
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

car = 차(2, 1000)
print(car.바퀴)
print(car.가격)


# 
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(차):
    pass

#
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(차):
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
bicycle = 자전차(2,100)
print(bicycle.가격)


# 
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        self.바퀴 = 바퀴
        self.가격 = 가격
        self.구동계 = 구동계

bicycle = 자전차(2,100, "시마노")
print(bicycle.구동계)

# 부모 클래스에 이미 기능이 있으면 super로 사용 
class 차:
    def __init__(self, 바퀴, 가격):
        print("부모 클래스의 생성자 호출")
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        # 차.__init__(self, 바퀴, 가격) # super를 더 권장
        self.구동계 = 구동계

bicycle = 자전차(2,100, "시마노")
print(bicycle.구동계)

# 285 
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴,가격)

    def 정보(self):
        print("바퀴수: ", self.바퀴)
        print("가격: ", self.가격)

car = 자동차(4, 1000)
car.정보()

#
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴,가격)
    def 정보(self):
        print("바퀴수: ", self.바퀴)
        print("가격: ", self.가격)

class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴,가격)
        self.구동계 = 구동계
    def 정보(self): 
        print("바퀴수: ", self.바퀴)
        print("가격: ", self.가격)

bicycle = 자전차(2,100,"시마노")
bicycle.정보()


# 부모 클래스로 정보() 옮기기
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
    def 정보(self):
        print("바퀴수: ", self.바퀴)
        print("가격: ", self.가격)

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴,가격)


class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴,가격)
        self.구동계 = 구동계


bicycle = 자전차(2,100,"시마노")
bicycle.정보()


# 287
#  
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
    def 정보(self):
        print("바퀴수: ", self.바퀴)
        print("가격: ", self.가격)

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴,가격)


class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴,가격)
        self.구동계 = 구동계
    # overrid : 재정의 
    def 정보(self):
        super().정보()
        print("구동계", self.구동계) # 부모에 없는 기능을 정의해서 사용 

bicycle = 자전차(2,100,"시마노")
bicycle.정보()


# 288 : 자식 클래스가 부모를 오버라이드 
class 부모:
    def 호출(self):
        print("부모호출")

class 자식(부모):
    def 호출(self):
        print("자식호출")

나 = 자식()
나.호출()

# 289
class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
    def __init__(self):
        print("자식생성")

나 = 자식()

#290 : 부모를 명시적으로 생성 시 super 사용
class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
    def __init__(self):
        print("자식생성")
        super().__init__() # 부모를 명시적으로 호출

나 = 자식()