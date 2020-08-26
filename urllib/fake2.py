from urllib.request import urlopen
import urllib.request as request
from fake_useragent import UserAgent

url = 'https://sports.v.daum.net/v/20200824062100679'

try:
    user_agent = UserAgent()

    # 헤더 정보 생성
    headers = {'User-agent' : user_agent.chrome}
    request_url = request.Request(url, headers = headers)
    req = urlopen(request_url)
    res = req.read().decode('utf-8')
except Exception as e:
    print(e)
else:
    print('request header : {}'.format(request_url.header_items()))
    print('response header : {}'.format(req.info()))
