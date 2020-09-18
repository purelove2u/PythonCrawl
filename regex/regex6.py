import openpyxl
import re

# 엑셀 파일 로드
excel_file = openpyxl.load_workbook('./resources/train.xlsx')

pattern = re.compile(r' [A-z]+\.')

# 현재 Active Sheet 얻기
sheet1 = excel_file.active

for each_row in sheet1.rows:
    print(each_row[3].value)
    print(pattern.findall(each_row[3].value))

excel_file.close()
