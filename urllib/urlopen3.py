# urlopen() : 요청하는 url의 정보를 메모리에 올려서 분석할 때 사용
import urllib.request as req
from urllib.error import HTTPError
from urllib.parse import urlparse

encar_url = "http://www.encar.com/index.do"

try:
    response = req.urlopen(encar_url)

    # 수신된 정보 확인
    print("type : {}".format(type(response)))
    print("geturl : {}".format(response.geturl()))
    print("status : {}".format(response.status))
    print("header : {}".format(response.getheaders()))
    print("getcode : {}".format(response.getcode()))
    print("parse : {}".format(urlparse("http://www.encar.com?test=test")))

    contents = response.read().decode("euc-kr")
    # text = data.decode("utf-8")
except HTTPError as e:
    print(e)
else:
    # print("Header Info - {}".format(response.info()))
    print(contents[:4000])


