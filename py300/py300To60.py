# 리스트
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

# 리스트에 값 추가 
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)

# 사이에 추가 
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.insert(1,"수퍼맨")
print(movie_rank)

# 리스트 삭제 
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
del movie_rank[2]
print(movie_rank)

# 삭제 
movie_rank = ["닥터 스트레인지", "스플릿", "럭키", "배트맨"]
movie_rank = movie_rank[0:2]
print(movie_rank)

# 더해서 새로운 리스트 만들기
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 최대값, 최소값
nums = [1,2,3,4,5,6,7]
print(max(nums))
print(min(nums))

print(sum(nums))

# 리스트의 길이 
cook = ["피자", "김밥", "만두"]
print(len(cook))

# 평균은 함수가 없음 
nums = [1,2,3,4,5,6,7]
print(sum(nums)/len(nums))
