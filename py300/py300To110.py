# boolean type
a = True
print(type(a))

# False : 3==5
a = 3 ==5 
print(a)

print(3==5) # False로 출력

print(3<5) # True 출력

x =4
print(1<x<5)  # True 출력

print( (3==3) and (4!=3)) # True 출력

# print(3=>4) # 오류 출력 : 표시 순서 오류
print(3>=4)   # 정상 출력 : 표시 순서 정상

if 4<3:
    print("Hello world")
print("next Hello") # 다음 코드 수행

# if else : Hi, there 출력
if 4<3:
    print("Hello")
else:
    print("Hi, there")    

# 1 2 4 출력
if True:
    print("1")
    print("2")
else:
    print("3")
print("4")

# 3 5 출력 확인 가능 
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")