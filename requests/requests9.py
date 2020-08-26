import requests

with requests.Session() as s:
    res = s.get("https://jsonplaceholder.typicode.com/users", stream=True)
    # print("json : {}".format(res.json()))
    for person in res.json():
        for k, v in person.items():
            print("{} : {}".format(k, v))
        print()
