import re
import openpyxl

# ' VS '로 문자열 분리하기
string = 'python VS java'
pattern = re.compile(r' VS ')
print(pattern.split('python VS java'))
print()

# 주민번호의 - 기호를 *로 바꿔서 출력하기
string = '801210-1011323'
print(re.sub('-', '*', string))
print()
########답안코드
pattern = re.compile(r"-")
print(pattern.sub("*", string))
print(re.sub(pattern, "*", string))

# data_kr.xlsx 를 읽어서 주민번호 뒷자리를 *로 바꿔서 출력하기
excel_file = openpyxl.load_workbook('./resources/data_kr.xlsx')

sheet1 = excel_file.active

for each_row in sheet1.rows:
    front_num = each_row[1].value[:6]
    back_num = each_row[1].value[7:]
    # print(back_num)
    result = re.sub('.','*', back_num)
    print(front_num + '-' + result)
    # print(each_row[1].value[7:])

################답안코드############################
pattern = re.compile(r"[0-9]{7}") # 연속된 숫자 7개 검출하는 표현식

for item in sheet1.rows:
    print(re.sub(pattern, "*******", item[1].value))
