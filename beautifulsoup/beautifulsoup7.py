# gmarket 카테고리 가져오기
import requests
from bs4 import BeautifulSoup

url = 'https://www.gmarket.co.kr'
res = requests.get(url)

# 파싱
soup = BeautifulSoup(res.content, 'html.parser')

category = soup.findAll('span', {'class':'link__1depth-item'})
#print('카테고리 : {}'.format(category))

for depth in category:
    print(depth.string)

print()

two_depth = soup.findAll('a', 'link__2depth-item')
# print(two_depth)
for depth in two_depth:
    print(depth.string)


print()
# 2 depth category 추출
two_depth = soup.find_all("li", "list-item__2depth")
# print(two_depth)
for depth in two_depth:
    # print(depth)
    link1 = depth.find("a")["href"]
    print(link1, depth.string)
