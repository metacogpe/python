a ="3" ; b="4"
print(a+b)  # 34 로 출력 : 문자열 연결

print("Hi" * 3) # 반복 출력

print("_" *80)  # _____________   출력

t1 = "python"
t2 = "java"
t = t1 + ' ' +t2
print(t)
print(t*5)

# formatting
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s  나이: %d"  % (name1, age1))

# format method 
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {}  나이: {}".format(name1, age1))

# fstring : 코드 읽기가 쉬움 :3.6부터 지원
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름 : {name1}  나이: {age1}")

# 컴마 제거하기 
상장주식수 ="5,969,782,550"
a = int(상장주식수.replace(',','')) 
print(a)

# 슬라이싱
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 공백 제거 
data = "   삼성전자   "
data = data.strip() # 좌우공백 제거 
print(data, len(data))


