#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint

def lists(item):
	data_string = urllib.quote(json.dumps({'id': 'data_explorer'}))

	action = '%s_list' %item

	# Make the HTTP request.
	url = 'https://data.hdx.rwlabs.org/api/action/%s'%action

	#url = 'http://demo.ckan.org/api/3/action/group_list'
	response = urllib2.urlopen(url,
	        data_string)
	assert response.code == 200

	# Use the json module to load CKAN's response into a dictionary.
	response_dict = json.loads(response.read())

	# Check the contents of the response.
	assert response_dict['success'] is True
	result = response_dict['result']
	return result

def package_list():
	return lists("package")

def tags_list():
	return lists("tag")

def group_list():
	return lists("group")


get_attrib = lambda attrib,x: map(lambda k: k[attrib],x)
 
tag_names = lambda x: get_attrib("name",x['tags'])

def packages_by_tags(tags):
	ids = package_list()
	

	for t in (x for x in ids if any(map(lambda y: y in tag_names(show_package(x)) ,tags))):
		print t

def get_ors_sahel():
	data_string = urllib.quote(json.dumps({'resource_id': '735b3f3a-eef6-4eb4-8b43-9307bac3177c'}))
	action = 'datastore_search'
	url = 'https://data.hdx.rwlabs.org/api/action/%s'%action

	response = urllib2.urlopen(url,
	        data_string)
	assert response.code == 200

	# Use the json module to load CKAN's response into a dictionary.
	response_dict = json.loads(response.read())

	# Check the contents of the response.
	assert response_dict['success'] is True
	result = response_dict['result']
	return result

def show_tags(id):
	return show('tag',id)['packages']

def show_package(id):
	return show('package',id)
	
def show(item,item_id):
	data_string = urllib.quote(json.dumps({'id': item_id}))
	action = '%s_show' % item
	url = 'https://data.hdx.rwlabs.org/api/action/%s'%action
	
	response = urllib2.urlopen(url,
	        data_string)

	assert response.code == 200

	# Use the json module to load CKAN's response into a dictionary.
	response_dict = json.loads(response.read())

	# Check the contents of the response.
	assert response_dict['success'] is True
	result = response_dict['result']
	return result

def get_ors_tags():
	data_string = urllib.quote(json.dumps({'id': 'ors'}))
	action = 'tag_show'
	url = 'https://data.hdx.rwlabs.org/api/action/%s'%action

	response = urllib2.urlopen(url,
	        data_string)
	assert response.code == 200

	# Use the json module to load CKAN's response into a dictionary.
	response_dict = json.loads(response.read())

	# Check the contents of the response.
	assert response_dict['success'] is True
	result = response_dict['result']
	return result

if __name__ == '__main__':
	#print get_ors_tags()
	pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(get_ors_tags())

