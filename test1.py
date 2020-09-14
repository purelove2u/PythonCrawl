n = int(input("합을 구하고 싶은 정수를 입력하세요 : "))
print('*' * 30)
print('1부터 {}까지 정수의 합 구하기'.format(n))
print('*' * 30)
sum = 0
for i in range(1, n+1):
    sum = sum + i
print('1 ~ {}의 합 : {}'.format(n, sum))