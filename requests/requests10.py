import requests
import json

with requests.Session() as s:
    res = s.get("https://httpbin.org/stream/10", stream=True)
    print("encoding {}".format(res.encoding))  # None

    # print(res.json()) => 에러 발생

    if res.encoding is None:
        res.encoding = "UTF-8"
        print("encoding {}".format(res.encoding))  # None

    for line in res.iter_lines(decode_unicode=True):
        print(line)
        print(type(line))

        # str => dict
        item = json.loads(line)

        for k, v in item.items():
            print("{} : {}".format(k, v))

