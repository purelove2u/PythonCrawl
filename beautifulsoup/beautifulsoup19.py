import openpyxl

# temp4.xlsx 읽어오기
excel_file = openpyxl.load_workbook("./resources/temp4.xlsx")

# 읽어올 시트 명 지정하기
sheet1 = excel_file["팁과 강좌"]

# 데이터 읽어오기
for item in sheet1.rows:
    print(item[0].value, item[1].value)


# 엑셀파일 종료
excel_file.close()
