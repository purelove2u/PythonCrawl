
menu = int(input('어떤 커피를 드릴까요? (1:보통, 2:설탕, 3:블랙)'))

def coffee_machine(menu):
    print('1. (자동으로) 뜨거운 물을 준비한다.')
    print('2. (자동으로) 종이컵을 준비한다.')
    if menu == 1:
        print('3. (자동으로) 보통 커피를 탄다.')
    elif menu == 2:
        print('3. (자동으로) 설탕 커피를 탄다.')
    elif menu == 3:
        print('3. (자동으로) 블랙 커피를 탄다.')
    else:
        print('3. (자동으로) 아무거나 탄다.')
    print('4. (자동으로) 물을 붓는다.')
    print('5. (자동으로) 스푼으로 저어서 녹인다.')
    print()
    print('손님 커피 여기 있습니다.')

coffee_machine(menu)