import requests

with requests.Session() as s:
    res = s.get("https://api.github.com/events", timeout=0.001)
    print(res.text)
