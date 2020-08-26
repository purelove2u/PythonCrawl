import urllib.request as request
from urllib.error import URLError, HTTPError

target_url = [
    "https://www.naver.com",
    "http://ph.spotvnews.co.kr/news/photo/201707/150270_181475_2728.jpg"
]

path_list = [
    "d:/download/naver.html",
    "d:/download/secret_forest.jpg"
]

# for url in target_url:
for i, url in enumerate(target_url):
    try:
        # 정보 가져오기
        response = request.urlopen(url)
        # 정보 읽기
        contents = response.read()
        # 상태 정보 확인
        print("-" * 50)
        print("header info - {} : {}".format(i, response.info()))
        print("Http status code - {}".format(response.getcode()))
        print()

        # 파일 저장(w:write, b:byte)
        with open(path_list[i], 'wb') as f:
            f.write(contents)

    except HTTPError as e1:
        print(e1)
    except URLError as e2:
        print(e2)
    else:
        print('성공')
