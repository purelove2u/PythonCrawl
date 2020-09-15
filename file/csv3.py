import csv

with open("./resources/sample2.csv", "r") as f:
    reader = csv.reader(f, delimiter='|')
    # print(reader)
    # print(type(reader))
    # print(dir(reader))
    next(reader)  # 헤더명 없애기

    for c in reader:
        print(c)
