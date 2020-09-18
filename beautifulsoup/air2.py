import requests
from urllib.parse import unquote
from bs4 import BeautifulSoup

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'

# 인코딩되어 넘어온 서비스키를 또 재차 인코딩시켜서 넘겨주는 바람에 오류가 남
# - > unquote를 사용하여 디코딩 후 넘겨주어 문제 해결
param = {
    'serviceKey' : unquote('p%2Fap74MNNEEhIu9WdWFtJ%2FO%2FIkANeiOaXF8CePmug9yc0BJnfLG3fcYabIjwJS2cbaSX0EMGwLBHv5Pf5SV%2BvQ%3D%3D'),
    'stationName' : '양천구',
    'dataTerm' : 'daily'
}

res = requests.get(url, params=param)
# print(res.text)
soup = BeautifulSoup(res.content, 'html.parser')

data = soup.find_all('item')
for item in data:
    print(item.get_text())

