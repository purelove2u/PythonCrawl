import re

# 정규식
# sub() : 찾고 바꾸기
# match() : 문자열 처음부터 정규식과 매칭되는 패턴을 찾아서 리턴
# search() : 문자열 전체를 검색해서 정규식과 매칭되는 패턴을 찾아서 리턴

pattern = re.compile('[a-z]+')
matched = pattern.match('Dave')
print('match() : ', matched)
#match() :  None
searched = pattern.search('Dave')
print('search() : ', searched)
#search() :  <re.Match object; span=(1, 4), match='ave'>

print()
print('***  찾고 바꾸기 ***')
pattern = re.compile('D[.]A')

string = 'DDA D1A DDA DA'
# re.sub(패턴, 바꿀문자열, '원본문자열')
result = re.sub('D.A', 'Dave', string)
print(result)

result = re.sub(pattern, "Dave", string)
print(result)

# findall() : 정규표현식과 매칭되는 모든 문자열을 리스트 객체로 리턴
print()
pattern = re.compile('[a-z]+')
print(pattern.findall('Game of Life in Python'))

# split() : 찾은 정규표현식 패턴 문자열을 기준으로 문자열 분리
print()
pattern = re.compile(':')
print(pattern.split('python:java'))

