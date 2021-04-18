import requests  # python -m pip install requests
import datetime 
 
r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")
bitcoin = r.json() 

timestamp = bitcoin['timestamp'] 
date = datetime.datetime.fromtimestamp(timestamp/1000)
print(date)
print(bitcoin['bid'])
print(bitcoin['ask'])
print(bitcoin['volume'])
print(r.text)

# pandas series 사용 이유
from pandas import Series   # python -m pip install pandas
s = Series([100, 200, 300, 400])
print(s /10)    # list 와 달리 사칙 연산 가능


# dataframe 
from pandas import DataFrame
data = {"open": [737, 750], "high": [755, 780], "low": [700, 710], "close": [750, 770]} 
df = DataFrame(data , index=["2018-01-01", "2018-01-02"]) 
print(df)



import requests
import pandas as pd
my_url="https://stockplus.com/m/stocks/KOREA-A005930/analysis"
table=pd.read_html(my_url)
  

  
import pandas as pd 
from bs4 import BeautifulSoup as bs
url = "https://finance.naver.com/item/sise_day.nhn?code=066570" 

response = requests.get(url, headers=headers)

html = bs(response.text, "lxml")
html_table = html.select("table")
len(html_table)

df = pd.read_html(url) 
#print(df[0])