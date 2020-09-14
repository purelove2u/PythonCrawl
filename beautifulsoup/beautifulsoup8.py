# select, select_one 이용하기
# 앞의 find 와는 다르게 css 선택자를 이용해서 가져오기

from bs4 import BeautifulSoup

with open('./beautifulsoup/story.html', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
p1 = soup.select_one('p.title')
print(p1)
print(p1.string)
print(p1.text)
print(p1.get_text())

print()
print(soup.select_one("a#link1").string)

print()
print(soup.select_one("a[data-io='link3']").text)

print()
link1 = soup.select("p.story > a")
# print(link1)
for link in link1:
    print(link.string)


print()
print(soup.select('p.story > a:nth-of-type(2)'))
