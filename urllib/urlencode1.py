# urllib.parse 내 urlencode() 사용하기
# urlencode() - parameter value return 할 때 주로 사용
            # - ex) https://naver.com?search=영화

from urllib.request import urlopen
from urllib.parse import urlencode

api = "https://api.ipify.org"

url = api + "?" + "format=json"
print("요청 url : {}".format(url))

response = urlopen(url).read().decode('utf-8')
print(response)

