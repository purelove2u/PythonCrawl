# urllib.parse 내 urlencode() 사용하기
# urlencode() - parameter value return 할 때 주로 사용
            # - ex) https://naver.com?search=영화

from urllib.request import urlopen
from urllib.parse import urlencode

api = "https://api.ipify.org"
values = {"format" : 'json'}

# url = api + "?" + values                   
print('befor param : {}'.format(values))
params = urlencode(values)
print('after param : {}'.format(params))

url = api + '?' + params
print("요청 url : {}".format(url))

response = urlopen(url).read().decode('utf-8')
print(response)

