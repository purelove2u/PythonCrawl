import openpyxl

def write_excel_template(filename, sheetname, listdata):

    # 엑셀 파일 생성
    excel_file = openpyxl.Workbook()

    # 기본 sheet 활성화
    sheet1 = excel_file.active

    # 시트의 컬럼 너비 조정
    sheet1.column_dimensions['A'].width = 100
    sheet1.column_dimensions['B'].width = 20

    # 시트 이름 변경
    if sheet1.title != '':
        sheet1.title = sheetname

    # 시트에 데이터 저장
    for item in listdata:
        sheet1.append(item)

    # 엑셀 파일 저장
    excel_file.save('./resources/' + filename)

    # 엑셀 파일 종료
    excel_file.close()


if __name__ == '__main__':
    write_excel_template('temp2.xlsx', 'test', [['data1', 'data2', 'data3'],["이름", "나이"], ["홍길동", 25], ["김지수", 23], ["신지호", 26]])
