import requests

with requests.Session() as s:
    res = s.get("https://jsonplaceholder.typicode.com/todos/1", stream=True)
    print("json : {}".format(res.json()))
    print("headers : {}".format(res.headers))
    print("res.json().keys() : {}".format(res.json().keys()))
    print("res.json().values() : {}".format(res.json().values()))
    print("res.encoding : {}".format(res.encoding))
    print("res.content : {}".format(res.content))
    print("res.text : {}".format(res.text))
