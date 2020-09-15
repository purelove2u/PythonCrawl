import requests
from bs4 import BeautifulSoup
import os
import urllib.request as req

url = 'https://www.google.com/search?q=%ED%8A%B8%EB%9F%AD&sxsrf=ALeKk01u4duUXouAKK7nME8jGMqOYw2LUw:1600140182227&source=lnms&tbm=isch&sa=X&ved=2ahUKEwik25vZmurrAhVLFogKHeaIDsYQ_AUoAXoECA0QAw&cshid=1600140226807176&biw=1920&bih=920'

res = requests.get(url)

# 이미지 저장 경로
savePath = 'd:/download/'

# 폴더 생성
try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    print('폴더 생성 실패', e.filename)
else:
    print('폴더 생성')


# 이미지 태그 찾기

soup = BeautifulSoup(res.content, 'html.parser')
img_list = soup.select("div.bRMDJf.islir img")
print(img_list)

# for i, img in enumerate(img_list, 1):
#     # 저장파일명 및 경로
#     fullfilename = os.path.join(savePath, savePath + str(i) + '.png')
    
#     # 다운로드 요청
#     req.urlretrieve(img['src'], fullfilename)