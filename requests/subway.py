# 위키피디아 서울 지하철
# https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0

import requests

# url = "https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0"
url = "https://ko.wikipedia.org/wiki/서울_지하철"

contents = requests.get(url)
print(contents.text)


# 모듈로 만들어보기
def info():
    url = "https://ko.wikipedia.org/wiki/서울_지하철"

    res = requests.get(url)
    # print(res.text)
    print(res.content)  # byte형태로 출력


if __name__ == "__main__":
    info()
