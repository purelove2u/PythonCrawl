# fake-useragent : 자동으로 useragent를 만들 수 있음
#                  Browser에서 접근하는 것처럼 속이기 위해 사용

from fake_useragent import UserAgent

# 객체 생성
user_agent = UserAgent()

# user-agent 만들기
print(user_agent.ie)
print(user_agent.msie)
print(user_agent.chrome)
print(user_agent.safari)
print(user_agent.opera)
print(user_agent.firefox)
print(user_agent.random)
print(user_agent.edge)
