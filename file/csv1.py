# csv 저장하기
import csv

list1 = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9], 
    [10,11,12], 
    [13,14,15], 
    [16,17,18]
]

# with open('./resources/sample1.csv', 'w') as f:
#     wt = csv.writer(f)

#     for v in list1:
#         wt.writerow(v)

with open("./resources/sample1.csv", "w", newline="") as f:
    wt = csv.writer(f)
    wt.writerows(list1)
