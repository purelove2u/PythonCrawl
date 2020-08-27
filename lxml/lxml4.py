import requests
from lxml import etree

# lxml 문서구조
# lxml.html
# lxml.etree

def main():
    url = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1001"

    res = requests.get(url)
    parseData(res)

def parseData(res):
    # lxml 에서 파싱을 할 수 있는 구조로 변경
    root = etree.fromstring(res.content)
    # print(type(root)) # <class 'lxml.etree._Element'>

    channel = root.xpath("//channel")
    print(channel[0].tag)

    print("\n--link1 태그--")
    link1 = root.xpath("//link/text()")
    print(link1)

    print("\n--title 태그--")
    title = root.xpath("//title/text()")
    print(title)

    print("\n")
    items = root.xpath("//channel/item")
    for item in items:
        for data in item:
            print(data.tag, ":", data.text)
        print("\n")


if __name__ == "__main__":
    main()
