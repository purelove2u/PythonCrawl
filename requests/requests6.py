import requests
from fake_useragent import UserAgent

user_agent = UserAgent()
s = requests.Session()

headers = {"user-agent": user_agent.chrome}

res = s.get("http://httpbin.org/get", headers=headers)
print(res.text)
s.close()
