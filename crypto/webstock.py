import pandas as pd 
url = "https://finance.naver.com/item/sise_day.nhn?code=066570&page=1" 
df = pd.read_html(url) 
#print(df[0])

# import pandas as pd 
# import requests 

# html = requests.get('https://finance.naver.com/item/frgn.nhn?code=005930&page=1') 

# table = pd.read_html(html.text)


# import pandas as pd

# # url 복사, 붙여넣기
# url = 'https://finance.naver.com/marketindex/worldDailyQuote.nhn?marketindexCd=OIL_DU&fdtc=2&page=1'

# # 해당 url에 있는 데이터프레임 가져오기
# # 한글이 포함되어 있다 : encoding= 'utf-8'
# # 원하는 내용이 포함된 데이터프레임만 가져오고 싶다 : match = '원하는 내용'
# # 특정 행을 열 명으로 사용하고 싶다 : header = 0
# data = pd.read_html(url)
# print(data)