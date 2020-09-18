import openpyxl
import re

# 남자만 추출

# 엑셀파일 로드
excel_file = openpyxl.load_workbook("./resources/train.xlsx")
# [a-zA-Z]
pattern = re.compile(r" Mr\.")

# 현재 Active Sheet 얻기
sheet1 = excel_file.active

for each_row in sheet1.rows:
    # print(each_row[3].value)
    # print(pattern.findall(each_row[3].value))
    if len(pattern.findall(each_row[3].value)) > 0:
        # if pattern.findall(each_row[3].value)[0].strip() == "Mr.":
        if pattern.search(each_row[3].value):
            print(each_row[3].value)
            
excel_file.close()
