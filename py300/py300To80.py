my_variable = ()  # 튜플(순서 있지만 수정 불가)
print(type(my_variable))
print(len(my_variable))

movie_rank = ('닥터 스트레인지', '스필릿', '럭키')
print(movie_rank)

a = (1,) # 값이 하나라도 , 기호 표시
print(a, type(a))

# 튜플은 수정 불가 
t = (0,1,2)
# t[0] = 'a' # 에러 발생


t = 1,2,3,4  # 튜플 타입임
print(type(t))

t =('a','b','c')
t =('A','B','C')  # 새로운 변수로 새로운 튜플을 가리키도록 가능
print(t)

# 튜플을 리스트로 변환 
interest = ('삼성','LG', 'SK')
print(list(interest))

interest = ['삼성','LG','SK']
print(tuple(interest))

# 튜플 언패킹
temp = ( 'apple','banana', 'cake')
a,b,c = temp
print(a, b, c)

# 튜플 생성
a = range(2, 99, 2) # range 타입
print(tuple(a))     # 튜플 타입으로 변경

