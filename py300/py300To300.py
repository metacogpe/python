# 파일
f = open('D:/GitHub/python/py300/매수종목1.txt', mode='wt', encoding='utf-8')
f.write('005930\n')
f.write('005380\n')
f.write('035420\n')

f.close()

# 
f = open('D:/GitHub/python/py300/매수종목2.txt', mode='wt', encoding='utf-8')
f.write('005930 삼성전자\n')
f.write('005380 현대차\n')
f.write('035420 네이버\n')
f.close()

# csv, cp949 인코딩
import csv
f = open('D:/GitHub/python/py300/매수종목.csv', mode='wt', encoding='cp949', newline='')
writer = csv.writer(f)
writer.writerow(['종목명','종목코드','PER'])
writer.writerow(['삼성전자','005930','15.59'])
writer.writerow(['NAVER','035420','55.82'])
f.close()

# 294 : 파일 읽기
f = open('D:/GitHub/python/py300/매수종목1.txt', mode='rt', encoding='cp949', newline='')
lines = f.readlines()
codes =[]
for line in lines:
    code = line.strip() # '\n' 제거
    codes.append(code)
print(codes)
f.close()

# 딕셔너리에 저장
f = open('D:/GitHub/python/py300/매수종목2.txt', mode='rt', encoding='utf-8')
lines = f.readlines()

data = {}
for line in lines:
    line = line.strip()
    k, v = line.split()
    # print(k,v)
    data[k] = v
print(data)  # {'005930': '삼성전자', '005380': '현대차', '035420': '네이버'}
f.close()

# 예외 처리 
per = ['10.31','','8.0']
for i in per:
    try:
        print(float(i))
    except:
        print(0)

# 297
#
per = ['10.31','','8.0']
new_per = []
for i in per:
    try:
        v = float(i)
    except:
        v = 0
    new_per.append(v)
print(new_per)

#298
try:
    b = 3/0 
except ZeroDivisionError:
    print('0으로 나누면 안되요!')

try:
    a = float('') 
except ZeroDivisionError:
    print('0으로 나누면 안되요!')
except ValueError:
    print('Value Error')

# 299
data = [1,2,3]
for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e); print('인덱스 에러')

# 300 try except else finally
per = ['10.31','','8.0']
for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print('clean data')
    finally:
        print('변환완료')


