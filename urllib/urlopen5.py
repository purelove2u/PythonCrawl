# 네이버 / 다음 뉴스 가져오기
# 화면출력 / 파일 저장
import urllib.request as request
from urllib.error import URLError, HTTPError

target_url = "https://sports.v.daum.net/v/20200824055311099"
path_url = "d:/download/sportsnews.html"

try:
    response = request.urlopen(target_url)
    contents = response.read().decode("utf-8")
    print(contents)
    with open(path_url, 'w', encoding="utf-8") as f:
        f.write(contents)
    
except HTTPError as e1:
    print(e1)
except URLError as e2:
    print(e2)
else:
    print("성공")