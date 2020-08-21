# urlopen() : 요청하는 url의 정보를 메모리에 올려서 분석할 때 사용
import urllib.request as req

weather_url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"

data = req.urlopen(weather_url).read()

text = data.decode("utf-8")

print(text)