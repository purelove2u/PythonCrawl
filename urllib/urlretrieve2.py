# urlretrieve : 요청하는 url의 정보를 local 파일로 저장
#              csv, api data등 많은 양의 데이터를 한꺼번에 저장할 때 사용
import urllib.request as req
# 요청 url
img_url = "https://imgnews.pstatic.net/image/436/2020/08/21/0000038581_001_20200821085129065.jpg?type=w647"
html_url = "http://google.com"
# local file
save_html = "d:/google.html"
save_img = "d:/save1.png"

try:
    file1, header1 = req.urlretrieve(img_url, save_img)
    file2, header2 = req.urlretrieve(html_url, save_html)
except Exception as e :
    print(e)
else:
    print(header1)
    print("성공")
