# 행정안전부 사이트의 RSS 수진
# RSS : 새로운 소식이 업데이트 되어 있는지 알 수 있도록 해주는 것

from urllib.request import urlopen
from urllib.parse import urlencode

# 행정안전부 rss 기본 주소
api = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

print(params)

for c in params:
    param = urlencode(c)

    url = api + '?' + param

    print('url : {}'.format(url))

    # 요청
    contents = urlopen(url).read().decode('utf-8')
    print('+' * 50)
    print(contents)
    print()

