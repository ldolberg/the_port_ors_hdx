#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint

districts = ["bhaktapur","dhading","dolakha","gorkha",
 "kathmandu","kavrepalanchok" ,"lalitpur","makwanpur"  ,    "nuwakot","okhaldhunga" ,   "ramechhap"    ,  "rasuwa","sindhuli","sindhupalchowk"]




def get_coordinates(d):
	data_string = urllib.urlencode({'q': d,"maxRows":10,"username":"demo"})

	# Make the HTTP request.
	url = 'http://api.geonames.org/searchJSON'

	#url = 'http://demo.ckan.org/api/3/action/group_list'
	response = urllib2.urlopen(url,
	        data_string)
	#print url+data_string
	assert response.code == 200

	# Use the json module to load CKAN's response into a dictionary.
	response_dict = json.loads(response.read())

	# Check the contents of the response.
	#assert response_dict['success'] is True
	result = response_dict
	return (response_dict['geonames'][0]['lat'],response_dict['geonames'][0]['lng']) if len(response_dict['geonames']) > 0  else (0,0)


if __name__ == '__main__':
	print {d:get_coordinates(d) for d in districts}
		