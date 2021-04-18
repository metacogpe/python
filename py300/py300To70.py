# 슬라이싱
price= ['20170809', 100,130,140,150,160,170]
print(price[1:])

# 홀수
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[::2])

# 짝수
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[1::2])

# 리스트를 역방향 출력 : 역순
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[::-1])

# 특정 멤버만 출력
interest = ['삼성','LG','Naver']
print(interest[0], interest[1])

# join 메소드로 붙여서 
interest = ['삼성','LG','Naver']
result = ' '.join(interest) # 공백 포함 연결
print(result)

# 슬래시로 합치기 
interest = ['삼성','LG','Naver']
print('/'.join(interest))

# 리스트에 join으로 줄바꿈
interest = ['삼성','LG','Naver']
result = '\n'.join(interest)
print(result)

# 문자열 split
string = "삼성/LG/Naver"
result = string.split("/") # 리스트로 저장
print(result)  

# 정렬
data = [2,4,3,1, 5, 10, 9, 10]
data.sort() # 정렬되어 저장 : 원본을 정렬해도 되는 경우
print(data) 

data = [2,4,3,1, 5, 10, 9, 10]
data2 = sorted(data) # 정렬데이터는 원본은 그대로 두고 생성
print(data)
print(data2)