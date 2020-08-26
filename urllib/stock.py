from urllib.request import urlopen
import urllib.request as req
import json
import csv
from fake_useragent import UserAgent


user_agent = UserAgent()

headers = {
    "User-agent": user_agent.chrome,
    "referer": "http://finance.daum.net",
}

# 상위 10 개 항목
url = "http://finance.daum.net/api/search/ranks?limit=10"

# 요청
res = urlopen(req.Request(url, headers=headers)).read().decode("utf-8")
# print(res)
# json 다루기
rank_json = json.loads(res)["data"]
# print("중간 확인 : {}".format(rank_json))

# 데이터 저장을 위한 리스트
data = []
for ele in rank_json:
    print(
        "순위 : {}, 금액 : {}, 회사명 : {}".format(
            ele["rank"], ele["tradePrice"], ele["name"]
        )
    )
    data.append(ele)

    with open("d:/download/finance.txt", "a") as f, open(
        "d:/download/finance.csv", "w", newline=""
    ) as f1:
        # txt 저장
        f.write(
            "순위 : {}, 금액 : {}, 회사명 : {}\n".format(
                ele["rank"], ele["tradePrice"], ele["name"]
            )
        )
        # csv 저장
        output = csv.writer(f1)
        output.writerow(data[0].keys())  # header 부분
        for row in data:
            output.writerow(row.values())  # 값 부분
