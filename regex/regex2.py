import re

# 정규식
# . : 어떤 문자든 매칭
# ? : 최소 0 ~ 1
# * : 최소 0 ~ 무한대
# + : 최소 1 ~ 무한대

pattern = re.compile("D?A")
print("? : 최소 0 ~ 1")
print(pattern.search("A"))  # <re.Match object; span=(0, 1), match='A'>
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(pattern.search("AA"))  # <re.Match object; span=(0, 1), match='A'>

print()
pattern = re.compile("D*A")
print("* : 최소 0 ~ 무한대")
print(pattern.search("A"))
print(pattern.search("DA"))
print(pattern.search("DDDDDDDDDDDDA"))
# <re.Match object; span=(0, 13), match='DDDDDDDDDDDDA'>

print()
pattern = re.compile("D+A")
print("+ : 최소 1 ~ 무한대")
print(pattern.search("A"))  # None
print(pattern.search("DA"))
print(pattern.search("DDDDDDDDDDDDA"))
