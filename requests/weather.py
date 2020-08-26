# urlopen() : 요청하는 url의 정보를 메모리에 올려서 분석할 때 사용
# requests 라이브러리를 이용
import requests

weather_url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"

# 1. get 방식
# res = requests.get(weather_url)
# print(res.text)

# 2. session 방식
with requests.Session() as s:
    res = s.get(weather_url)
    print(res.text)