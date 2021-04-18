letters = "python"
print(letters[0:3]) # 3글자까지 출력 : 인덱싱

license_plate = "24가 2210"
print(license_plate[4:])
print(license_plate[-4:])

string ="홀짝홀짝홀짝"
print(string[0:6:2]) # 한 글자 건너뛰기
print(string[::2])  # 시작부터 끝까지 2씩 증가

string ="PYTHON"
print(string[::-1])  # 뒤집기 NOHTYP

phone_number = "010-1111-2222"  # 하이픈 제거
a = phone_number.replace("-", "") # a변수에 새로 생성
print(a)
print(phone_number)  # 최초 저장된 스트링

url = "http://sharebook.kr" #메모리에 url값을 바인딩
a = url.split(".")
print(a)

# lang ="python"
# lang[0] = 'P'  # 대문자 변환
# print(lang)  # 오류가 나므로 다른 방식으로 

string = "abcdef2a354a32a"
a = string.replace('a', "A") # a는 다른 메모리 영역
print(a)

string = "abcd"
a = string.replace('b','B')  # 변경된 문자열 신규 바인딩
print(string)
print(a)  # 새로 바인딩한 문자열






