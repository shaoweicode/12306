#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cli tickets check

Usage:
	tickets [-gdtkz] <from>  <to> <date>

Options:
	-h,--help show help
	-g 		  gaotie
	-d 		  dongche 
	-t        tekuai 
	-k        kauisu 
	-z        zhida 


Examples:
	tickets 北京 shanghai 2017-11-29
	tickets xia hefei 2017-11-29
"""

from docopt import docopt
import requests

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


def cli():
    arguments = docopt(__doc__)
    from_station = stations_dic.get(arguments['<from>'])
    to_station = stations_dic.get(arguments['<to>'])
    date = stations_dic.get(arguments['<date>'])
#goujian url
    url = 'https://kyfw.12306.cn/otn/lcsscx/query?purpose_codes=ADULTqueryDate={}&from_station={}&to_station={}'.format(date,from_station,to_station)
    r = requests.get(url,verify=False)
    print(r.json())


if __name__ == '__main__':
	cli()

    

