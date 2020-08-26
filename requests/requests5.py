import requests

s = requests.Session()

res = s.get("http://httpbin.org/cookies", cookies={"name": "hong"})
print(res.text)
s.close()
