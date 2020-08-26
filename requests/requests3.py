import requests

# 세션 활성화
s = requests.Session()
# 세션을 이용해 get 요청
# res = s.get("https://httpbin.org/get")

# 세션을 이용해 post 요청
# data = {"name": "hong"}
# res = s.post("https://httpbin.org/post", data=data)

# 세션을 이용해 delete 요청
# res = s.delete("https://httpbin.org/delete")

# 세션을 이용해 put 요청
data = {"name": "hong"}
res = s.put("https://httpbin.org/put", data=data)
print(res.text)

# 세션 종료
s.close()
