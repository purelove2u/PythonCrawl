# from urllib.request import urlopen
# from urllib.error import HTTPError
# from urllib.parse import urlencode
import requests

search_url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&'

param = {'query' : '영화'}

# param = urlencode(param)
# search_url += param

try:
    # contents = urlopen(search_url).read().decode('utf-8')
    contents = requests.get(search_url, params=param)
    print(contents.text[150000:200000])
except Exception as e:
    print("에러발생", e)