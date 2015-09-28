import urllib2
import urllib
import json
import pprint

distinct = lambda x: list(set(x))

def create_graph(packages):
	return [(x['id'],y['name'])  for x in packages for y in x['tags']]

def recommend_tags(p,idsAndTags):
	myTags = [x['name'] for x in  p['tags']]
	friends = distinct([x[0] for x in idsAndTags if any([t in x[1] for t in myTags]) if x[0] != p['id'] ])
	tagsOfFF = set()
	for f in friends:
		ftags = map(lambda x: x[1], filter(lambda x: x[0] == f ,idsAndTags))
		friendsofF = distinct([x for x in idsAndTags if any([t in x[1] for t in ftags]) if x[0] not in [p['id'],f] ])
		tagsOfFF = tagsOfFF.union(map(lambda x: x[1],friendsofF))
	return tagsOfFF


