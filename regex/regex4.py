import re

# 정규식 패턴
# [] : 괄호 안에 들어가는 문자 찾기
# [ - ] : 괄호 안에 문자를 범위 형태로 지정
# [^ ] : 괄호 안에 쓰여진 문자를 제외

pattern = re.compile('[abcdefgABCDEFG]')
print('[] : 괄호 안에 들어있는 문자 찾기')
print(pattern.search('a1234'))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search('z1234'))  # None

print()

pattern = re.compile("[a-gA-G]")
print("[] : 괄호안에 들어있는 문자 찾기 ")
print(pattern.search("a1234"))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search("z1234"))

print()

pattern = re.compile('[a-zA-Z0-9]')
print(pattern.search('1234---'))    #<re.Match object; span=(0, 1), match='1'>
print(pattern.search('------!@#$%^&&*-----')) #None
print(pattern.search("abcdefg"))

print()

pattern = re.compile('[^a-zA-Z0-9]')
print('[] : 괄호 안에 쓰여진 문자를 제외')
print(pattern.search('1234---'))    # <re.Match object; span=(4, 5), match='-'>
print(pattern.search('------!@#$%^&&*-----'))    # <re.Match object; span=(0, 1), match='-'>
print(pattern.search("abcdefg"))    # None

print()
pattern = re.compile("[가-힣]")
print("한글 찾기")
print(pattern.search("나"))     # <re.Match object; span=(0, 1), match='나'>
