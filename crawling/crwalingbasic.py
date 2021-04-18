import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import urllib.request
r1 = urllib.request.Request('https://m.stock.naver.com/item/main.nhn#/stocks/005930/total')
r2 = urllib.request.urlopen(r1)
r3 = r2.read()
r4 = r3.decode('utf-8')
r4.find('삼성')
print(r4)

#res = req.urlopen(url).read().decode('euc-kr')
