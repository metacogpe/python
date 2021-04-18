# module
import datetime # datetime.py, import를 통해 바인딩
now = datetime.datetime.now() # 함수 호출로 변수로 바인딩
print(now)

#
import datetime # datetime.py, import를 통해 바인딩
now = datetime.datetime.now() # 함수 호출로 변수로 바인딩
print(type(now)) # 일반적인 타입은 아니고 모듈 정의 타입

# 날짜를 더하는 timedelta
import datetime # datetime.py, import를 통해 바인딩
now = datetime.datetime.now() # 함수 호출로 변수로 바인딩
delta = datetime.timedelta(days=1)
print(now + delta)

# 날짜 빼기
import datetime # datetime.py, import를 통해 바인딩
for i in range(-5,0):
    delta = datetime.timedelta(days=i)
    print(now + delta)

#
# 시간
import datetime # datetime.py, import를 통해 바인딩
now = datetime.datetime.now() # 함수 호출로 변수로 바인딩
delta = datetime.timedelta(hours=1)
print(now + delta)


# 날짜만 strftime 함수
import datetime # datetime.py, import를 통해 바인딩
now = datetime.datetime.now() # 함수 호출로 변수로 바인딩
a = now.strftime('%Y %D %H:%M:%S')
print(a)

# 문자열을 시간타입으로 변경
import datetime
day = '2020-05-04'
ret=datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret)

# sleep : 현재시간 1초마다 출력
# import time
# import datetime
# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)
    
# 모듈 호출
import os             # os.rename()  ,권장되는 방식
from os import rename # rename()
from os import *      
import os as myos

# 
import os
ret = os.getcwd()
print(ret, type(ret))

# 
# import os
# os.rename("C:/befor.txt", "C:/after.txt")

#
import numpy
for i in numpy.arange(0,5, 0.1):
    print(i)

