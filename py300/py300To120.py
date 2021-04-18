# # 사용자 입력
# data = input("")
# print(data*2)

# # 숫자 입력 + 식
# data = input("숫자를 입력하세요 : ")
# print(int(data) + 10)


# # 짝수 홀수 판별
# data = input(">> ")
# data = int(data)
# if data % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")
# 200

# # 255를 초과하는지 여부 
# data = input("입력값 : ")
# data = int(data)
# data = data +20
# if data >255:
#     print(255)
# else:
#     print(data)

# #
# data = input("입력값:")
# data = int(data)
# if data <0:
#     print(0)
# elif data>255:
#     print(255)
# else:
#     print(data)

# data = input("현재시간:")
# if data[-2:] == "00": # 시간의 뒤에서 2자리만 보기 
#     print("정각입니다")
# else:
#     print("정각이 아닙니다")

# fruit = ["사과","포도","홍시"]
# data = input("좋아하는 과일은?")
# if data in fruit:
#     print("정답입니다.")
# else: 
#     print("오답입니다. ")

# # 종목 경고
# wan_invest_list = ["MS", 'KAKAO']
# item = input("종목입력: ")
# if item in wan_invest_list:
#     print("투자 경고")
# else: 
#     print("투자 정상")

# 계절 딕셔너리 
fruit ={"봄":"딸기","여름":"토마토","가을":"사과"}
season = input("종하하는 계절은?")
if season in fruit.keys():
    print("정답")
else:
    print("오답")


# 과일 입력 
fruit ={"봄":"딸기","여름":"토마토","가을":"사과"}
fruit_mem = input("종하하는 과일은?")
if fruit_mem in fruit.values():
    print("정답")
else:
    print("오답")