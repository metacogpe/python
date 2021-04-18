# # 대소문자 변환
# data = input("문자입력: ")
# if data.islower():
#     print(data.upper())
# else:
#     print(data.lower())


# # 점수 구간 학점 
# score = input("score : ")
# score = int(score)
# if score > 80:
#     print("grade is A")
# elif 60 < score <= 80:
#     print("grade is B")
# elif 40 < score <= 60:
#     print("grade is C")
# elif 20 < score <= 40:
#     print("grade is D")
# else:
#     print("grade is E")

# # 환율
# data = input("입력: ") # 100 달러
# tokens = data.split() 
# amount, currency = tokens # 언패킹
# amount = float(amount)

# if currency =='달러':
#     print(amount *1167)
# elif currency =='엔':
#     print(amount *1.096)
# elif currency =='유로':
#     print(amount *1268)
# else: 
#     print(amount *172)

# # 3개 중에 큰 수 출력
# num1 = int(input("input num1: "))
# num2 = int(input("input num2: "))
# num3 = int(input("input num3: "))

# if num1>num2 and num1 > num3:
#     print(num1)
# elif num2>num1 and num2 > num3:
#     print(num2)
# else:
#     print(num3)


# 휴대폰 앞자리로 구분
# number = input("휴대전화 번호 입력: ")   
# data = number[:3]
# if data == '011':
#     company = "SKT"
# elif data == '016':
#     company = "KT"
# elif data == '010':
#     company = "LGU"
# else:
#     company = "알수 없음" 
# print(f"당신은 {company} 사용자입니다.") # f string

# # 우편번호 : 앞의 3자리로 구 판별
# data = input("우편번호: ")
# data = data[:3] # 앞의 3자리
# if data in ["010","011","012"]:
#     print("강북구")
# elif data in ["013","014","015"]:
#     print("도봉구")
# elif data in ["016","017","018","019"]:
#     print("노원구")
# else:
#     print("알수 없음")

# 주민번호 뒷자리 중 남자/여자
# data = input("주민등록 번호: ")
# tokens = data.split("-") # 분리
# data2 = tokens[1]
# if data2[0] =='1' or data2[0] =='3':
#     print("남자")
# elif data2[0] =='2' or data2[0] == '4':
#     print("여자")
# else:
#     print("알수없음")

# 주민번호 지역코드 
# data = input("주민등록 번호: ")
# back = data.split("-")[1] # 분리후 슬라이싱
# if back[1:3] in ['00','01','02','03','04','05','06','07','08'] 
#     print("서울")
# else:
#     print("서울아님")

# # 주민번호 유효 판별 
# data = input("주민번호: ")
# data = data.replace("-","")
# calc1 = int(data[0]) * 2 + \
# int(data[1]) * 3 + \
# int(data[2]) * 4 + \
# int(data[3]) * 5 + \
# int(data[4]) * 6 + \
# int(data[5]) * 7 + \
# int(data[6]) * 8 + \
# int(data[7]) * 9 + \
# int(data[8]) * 2 + \
# int(data[9]) * 3 + \
# int(data[10]) * 4 + \
# int(data[11]) * 5 

# calc1 = calc1 % 11
# calc2 = (calc1 -11) * (-1)
# calc2 = str(calc2)
# if data[-1] == calc2[-1]:
#     print("유효")
# else:
#     print("비유효")


# 비트코인 가격정보 
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# print(btc)
open = float(btc['opening_price'])
high = float(btc['max_price'])
low = float(btc['min_price'])
diff = high -low
if (open+diff) > high:
    print("상승장")
else:
    print("하락장")

