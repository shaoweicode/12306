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

class TrainsCollections(object):
	"""docstring for TrainsCollections"""
	def __init__(self, available_trains,options):
		super(TrainsCollections, self).__init__()
		self.available_trains = available_trains
		self.options=options
    def get_information(self):
        for train in available_trains:
            train_list = train.split('|')
            train_no = train_list[3]
            initial = train_no[0].lower()
            if not self.options or initial in self.options:
                train = [
                        train_no,
                        '\n'.join([train_list[4],train_list[5]]),
                        '\n'.join([train_list[8],train_list[9]]),
                        train_list[10],
                        
                        
                        
                        
                        
                        
                        
                        ]
            
            
		



def cli():
    arguments = docopt(__doc__)
    from_station = stations_dic.get(arguments['<from>'])
    to_station = stations_dic.get(arguments['<to>'])
    date = arguments['<date>']
#goujian url
    url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,from_station,to_station)
    r = requests.get(url,verify=False)
    options = ''.join([key for key,value in arguments.items() if value is True])
    available_trains = r['data']['result']
    TrainsCollections(available_trains,options).pretty_print()
if __name__ == '__main__':
	cli()

#https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-12-01&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT    

