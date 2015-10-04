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
	print url+data_string

	#url = 'http://demo.ckan.org/api/3/action/group_list'
	response = urllib2.urlopen(url,
	        data_string)
	assert response.code == 200

	# Use the json module to load CKAN's response into a dictionary.
	response_dict = json.loads(response.read())

	# Check the contents of the response.
	#assert response_dict['success'] is True
	result = response_dict	
	try:
		return (response_dict['geonames'][0]['lat'],response_dict['geonames'][0]['lng']) if len(response_dict['geonames']) > 0  else (0,0)
	except Exception ,e:
		return (0,0) 

if __name__ == '__main__':
	districts = ["arghakhanchi"    ,"baglung"         ,"baitadi"         ,"bara"       ,    
"bhaktapur"       ,"bhojpur"         ,"chitawan"        ,"dang"            ,"dhading"    ,    
"dhankuta"        ,"dolakha"         ,"gorkha"          ,"gulmi"           ,"ilam"       ,    
"jhapa"           ,"kabhrepalanchok" ,"kanchanpur"      ,"kaski"           ,"kathmandu"  ,    
"khotang"         ,"lalitpur"        ,"lamjung"         ,"makawanpur"      ,"morang"     ,    
"mustang"         ,"myagdi"          ,"nawalparasi"     ,"nuwakot"         ,"okhaldhunga",    
"palpa"           ,"panchthar"       ,"parbat"          ,"parsa"           ,"ramechhap"  ,    
"rasuwa"          ,"rupandehi"       ,"sankhuwasabha"   ,"sarlahi"         ,"sindhuli"   ,    
"sindhupalchok"   ,"siraha"          ,"solukhumbu"      ,"sunsari"         ,"syangja"    ,    
"tbd"             ,"tanahu"          ,"taplejung"       ,"udayapur"        ,"lalitpur"   ,    
"sindhuli"]
	print json.dumps({d:get_coordinates(d) for d in districts})
		