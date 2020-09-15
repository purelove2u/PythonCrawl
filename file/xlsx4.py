import openpyxl

excel_file = openpyxl.Workbook()

# 기본 시트 활성화
sheet1 = excel_file.active

list1 = [
    ["name", "birth"],
    ["홍길동", "981225"],
    ["송혜교", "801025"],
    ["남주혁", "880705"],
    ["김지원", "860912"],
]

for idx, row in enumerate(list1, 2):
    sheet1.append(row)
    # 이미지 삽입
    img = openpyxl.drawing.image.Image("./resources/cat.png")
    img.width = 30
    img.height = 20
    sheet1.add_image(img, "C" + str(idx))

excel_file.save('./resources/test3.xlsx')

