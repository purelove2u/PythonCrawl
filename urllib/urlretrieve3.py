# urlretrieve : 요청하는 url의 정보를 local 파일로 저장
#              csv, api data등 많은 양의 데이터를 한꺼번에 저장할 때 사용
import urllib.request as req
# 요청 url
img_url = "https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile28.uf.tistory.com%2Fimage%2F99C7D2495DC168921334C4"
# local file
save_img = "d:/save2.png"

try:
    file1, header1 = req.urlretrieve(img_url, save_img)
except Exception as e :
    print(e)
else:
    print(header1)
    print("성공")
