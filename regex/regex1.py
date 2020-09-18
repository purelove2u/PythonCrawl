# 파이썬 정규식
import re

# 정규식 패턴 생성
pattern = re.compile('D.A')

# search : 패턴이 매칭되는 여부 확인
result = pattern.search('DAA')
print(result)   # <re.Match object; span=(0, 3), match='DAA'>

result = pattern.search("D1A")
print(result)

result = pattern.search("D00A")
print(result)

result = pattern.search("DA")
print(result)

result = pattern.search("d0A")
print(result)

result = pattern.search("d0A D1A 0111")
print(result)