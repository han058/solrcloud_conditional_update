#!/usr/bin/env python
#coding:utf8

"""
up.py : Conditional Update Code for Apache SolrCloud
"""

__author__ = "Han-young Park"
__copyright__ = "Copyright 2017, han058. Licensed to PSF under a Contributor Agreement."
__credits__ = ["Han-young Park"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Han-young Park"
__email__ = "han058@gmail.com"
__status__ = "Production"

import requests
from optparse import OptionParser
import random

def get_comma_sep_args(option, opt, value, parser):
	setattr(parser.values, option.dest, value.split(','))

def make_data(id, u_fueld):
	FORM = "{'%s':'%s','%s':{'set':'%s'}}"
	disp_str = FORM % (id, id_val, u_field, u_field_val)
	return disp_str

def update(host, port, collection, data):
	url = "http://%s:%s/solr/%s/update?commit=false" % ( host, port, collection )
	res = requests.get(url=url, data=data, headers={'Content-type':'application/json'})
	if res.code != 200:
		print "Fail to update!"
	else:
		print "Success to update!"

if __name__ == "__main__":
	usage = """usage: %prog [options]
	ex) %prog -i unique_document_id -f field_to_update -s server1,server2,server3,..
	"""
	parser = OptionParser(usage=usage)
	parser.add_option("-c", "--collection", type="string", dest="collection", help="Solr collection name", default="")
	parser.add_option("-p", "--port", type="string", dest="port", help="SolrCloud service port", default="8983")
	parser.add_option("-i", "--id", type="string", dest="id", help="Unique Document ID Field name in Solr shcema.xml", default="")
	parser.add_option("-f", "--field", type="string", dest="field", help="Single Field name to update value", default="")
	parser.add_option("-s", "--server", type="string", action="callback", callback=get_comma_sep_args, 	help="Solr Cloud server list", default="")

	(options, args) = parser.parse_args()

	parser.print_help()
