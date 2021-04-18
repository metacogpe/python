# 별 표현식
a, b = (1,2)
print(a,b)

#위와 달리 갯수가 맞지 않을 경우 
a, b, *c = (0,1,2,3,4,5)
print(a)
print(b)
print(c) # 리스트로 반영

scores = [8.8,8.9,8.7,9.2,9.3,9.7,9.9,9.5,7.8,9.4]
*valid_score, a, b = scores
print(valid_score) # a = 7.8, b = 9.4 이외는 valid_scoreㄷ

# 체조 점수 구하기 : 최고/최저 제거 
scores = [8.8,8.9,8.7,9.2,9.3,9.7,9.9,9.5,7.8,9.4]
scores.sort()
a, *score, b = scores  
print(a); print(score); print(b)
print(sum(score)/len(score)) # 평균

# 우측 8개만 변수에 바인딩 
scores = [8.8,8.9,8.7,9.2,9.3,9.7,9.9,9.5,7.8,9.4]
_, *score, _ = scores  # 사용하지 않을 값은 변수 불필요 
print(sum(score)/len(score)) # 평균


scores = [8.8,8.9,8.7,9.2,9.3,9.7,9.9,9.5,7.8,9.4]
_, _, *valid_score = scores  # 왼쪽 2개는 제외 
print(valid_score)

# 가운데 값만 변수로 바인딩
scores = [8.8,8.9,8.7,9.2,9.3,9.7,9.9,9.5,7.8,9.4]
_, *valid_score, _ = scores   
print(valid_score)

# 비어있는 딕셔너리 만들기 
temp = {}
print(temp, type(temp))

# 라벨을 붙일 수 있는 딕셔너리
ice = {"메로나":1000, 
       "폴라포":1200,
       "빵빠레":1800}
print(ice)

# 딕셔너리에 추가 : 순서없는 딕셔너리
ice = {"메로나":1000, 
       "폴라포":1200,
       "빵빠레":1800}
ice["죠스바"] =1200
ice["월드콘"] =1500
print(ice)


#특정 멤버 출력
ice = {"메로나":1000, 
       "폴라포":1200,
       "빵빠레":1800}
print("메로나 가격:",ice["메로나"])

# 멤버 수정
ice = {"메로나":1000, 
       "폴라포":1200,
       "빵빠레":1800}
ice["메로나"] = 1300
print(ice)

# 멤버 삭제 
ice = {"메로나":1000, 
       "폴라포":1200,
       "빵빠레":1800}
del ice["메로나"]
print(ice)

# 에러 발생
# 존재하지 않는 키로는 인덱싱 불가 

