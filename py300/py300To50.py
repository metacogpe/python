# 대문자
ticker = "btc_krw"
ticker = ticker.upper()
print(ticker)

# 소문자 
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)

# 문자열의 첫글자만 대문자로 
a = "hello"
a = a.capitalize()
print(a)

# endwith : 특정단어로 끝나는지 확인
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx")) 

# 여러 옵션으로 체크
file_name = "보고서.xls"
print(file_name.endswith(("xlsx", "xls"))) 

# startswith
file_name = "2020_보고서.xlsx"
print(file_name.startswith("20"))

#split
a = "hello world"
print(a.split())

ticker = "btc_krw"
print(ticker.split('_'))

date ="2020-05-01"
print(date.split('-'))

data ="039490   "
print(data.rstrip()) # 오른 공백 제거



