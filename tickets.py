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

def cli():
	arguments = docopt(__doc__)
	print(arguments)

if __name__ == '__main__':
	cli()