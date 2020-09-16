import openpyxl

# 엑셀파일 생성
excel_file = openpyxl.Workbook()

# default sheet 활성화
sheet1 = excel_file.active

# 시트 이름 변경
sheet1.title = '실습'

# 데이터 추가하기
sheet1.append(['data1', 'data2', 'data3'])

# 엑셀 파일 저장
excel_file.save('./resources/temp.xlsx')

# 엑셀 파일 종료
excel_file.close()
