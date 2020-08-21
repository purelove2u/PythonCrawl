# urlopen() : 요청하는 url의 정보를 메모리에 올려서 분석할 때 사용
import urllib.request as req
from urllib.error import HTTPError

best_url = "http://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"

try:
    response = req.urlopen(best_url)
    contents = response.read().decode("euc-kr")
    # text = data.decode("utf-8")
except HTTPError as e:
    print(e)
else:
    print("Header Info - {}".format(response.info()))
    print(contents[:4000])


