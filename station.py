import requests
from pprint import pprint



url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9031"
response = requests.get(url,verify=False)
stations = response.text

index = stations.index('=')
stations = stations[20:-2]
stations = stations.split('|')
stations_dic = {}
i=1
while i < len(stations):
    stations_dic[stations[i]]=stations[i+1]
    i=i+5