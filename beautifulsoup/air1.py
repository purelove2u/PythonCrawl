import requests

serviceKey = "p%2Fap74MNNEEhIu9WdWFtJ%2FO%2FIkANeiOaXF8CePmug9yc0BJnfLG3fcYabIjwJS2cbaSX0EMGwLBHv5Pf5SV%2BvQ%3D%3D"
stationName = "중랑구"
dataTerm = "DAILY"

url = (
    "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=" 
    + serviceKey 
    + "&stationName=" 
    + stationName 
    + "&dataTerm=" 
    + dataTerm
)


# url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
# param = {
#     'serviceKey' : 'p%2Fap74MNNEEhIu9WdWFtJ%2FO%2FIkANeiOaXF8CePmug9yc0BJnfLG3fcYabIjwJS2cbaSX0EMGwLBHv5Pf5SV%2BvQ%3D%3D',
#     'stationName' : '양천구',
#     'dataTerm' : 'daily'
# }

# res = requests.get(url, params=param, encoding='UTF-8')
res = requests.get(url)
# print(res.url)
print(res.text)

