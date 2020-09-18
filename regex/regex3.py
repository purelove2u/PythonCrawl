import re

# 정규식 패턴
# {n} : n 숫자만큼 반복
# {n,m} : 최소 n ~ 최대 m 반복

pattern = re.compile("AD{2}A")
print("{n} 사용법")
print(pattern.search("ADA"))  # None
print(pattern.search("ADDA"))  # <re.Match object; span=(0, 4), match='ADDA'>
print(pattern.search("ADDDA"))  # None

print()

pattern = re.compile("AD{2,6}A")
print("{n,m} 사용법")
print(pattern.search("ADDA"))
print(pattern.search("ADDDA"))
print(pattern.search("ADDDDDDA"))
