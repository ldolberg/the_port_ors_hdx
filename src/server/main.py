import os
from flask import Flask
from flask import request
from flask import jsonify
import json
import random

from flask import Flask
import district_distance 
import feedback

districts = json.loads('''{"kavrepalanchok": ["27.58333", "85.66667"], "dolakha": ["27.68027", "86.0701"], 
"lalitpur": ["27.67658", "85.31417"], "dhading": ["27.86424", "84.9283"], 
"bhaktapur": ["27.67298", "85.43005"], "ramechhap": ["27.32207", "86.05913"], 
"makwanpur": ["27.41667", "85.25"], "kathmandu": ["27.70169", "85.3206"], 
"nuwakot": ["28", "83.83333"], "sindhuli": ["27.2799", "85.98421"], 
"rasuwa": ["27.08617", "86.42758"], "okhaldhunga": ["27.31032", "86.50502"], 
"gorkha": ["28.00242", "84.62009"], "sindhupalchowk": [0, 0],"kanchanpur": ["28.83333", "80.33333"], "palpa": ["27.75", "83.83333"], "sankhuwasabha": ["27.58333", "87.33333"], "rupandehi": ["27.66667", "83.41667"], "gulmi": ["28.06941", "83.24536"], "arghakhanchi": ["27.91667", "83.08333"], "bara": ["26.75", "81"], "morang": ["-37.65", "145.1"], "parsa": ["34.92466", "68.64761"], "sindhuli": ["27.2799", "85.98421"], "makawanpur": ["27.41429", "85.17962"], "dhankuta": ["26.98333", "87.33333"], "sarlahi": ["27", "85.58333"], "kaski": ["28.33333", "84"], "chitawan": ["27.68333", "84.43333"], "baglung": ["28.27189", "83.58976"], "panchthar": ["27.16667", "87.83333"], "kabhrepalanchok": [0, 0], "khotang": ["27.25", "86.83333"], "okhaldhunga": ["27.31032", "86.50502"], "gorkha": ["28.00242", "84.62009"], "baitadi": ["29.57113", "80.43722"], "taplejung": ["27.35", "87.66667"], "ilam": ["33.6374", "46.4227"], "mustang": ["29.18321", "83.95634"], "lalitpur": ["27.67658", "85.31417"], "rasuwa": ["27.08617", "86.42758"], "solukhumbu": ["27.75", "86.75"], "sunsari": ["26.66667", "87.16667"], "bhojpur": ["25.30886", "84.44504"], "dang": ["31.0699", "120.87635"], "parbat": ["35.23731", "74.58914"], "syangja": ["28.09596", "83.87243"], "lamjung": ["28.48914", "84.1884"], "nawalparasi": ["27.66667", "83.91667"], "tbd": ["33.22661", "69.77123"], "siraha": ["26.65411", "86.2087"], "dolakha": ["27.68027", "86.0701"], "dhading": ["27.86424", "84.9283"], "sindhupalchok": ["27.82936", "85.54504"], "bhaktapur": ["27.67298", "85.43005"], "ramechhap": ["27.32207", "86.05913"], "jhapa": ["22.57314", "89.39283"], "tanahu": ["27.91667", "84.25"], "nuwakot": ["28", "83.83333"], "udayapur": ["26.94167", "86.52031"], "kathmandu": ["27.70169", "85.3206"], "myagdi": ["28.58333", "83.33333"]}''')

humanitarian = json.loads('''{
 "District": [ "", "arghakhanchi", "arghakhanchi", "baglung", "baglung", "baitadi", "bara", "bhaktapur", "bhaktapur", "bhaktapur", "bhojpur", "bhojpur", "bhojpur", "chitawan", "chitawan", "chitawan", "dang", "dhading", "dhading", "dhading", "dhading", "dhankuta", "dhankuta", "dolakha", "dolakha", "dolakha", "gorkha", "gorkha", "gorkha", "gulmi", "gulmi", "ilam", "jhapa", "kabhrepalanchok", "kabhrepalanchok", "kabhrepalanchok", "kanchanpur", "kaski", "kaski", "kaski", "kathmandu", "kathmandu", "kathmandu", "khotang", "khotang", "khotang", "lalitpur", "lalitpur", "lalitpur", "lamjung", "lamjung", "makawanpur", "makawanpur", "makawanpur", "morang", "mustang", "mustang", "myagdi", "myagdi", "nawalparasi", "nawalparasi", "nuwakot", "nuwakot", "nuwakot", "nuwakot", "okhaldhunga", "okhaldhunga", "okhaldhunga", "palpa", "palpa", "panchthar", "panchthar", "parbat", "parbat", "parsa", "ramechhap", "ramechhap", "ramechhap", "rasuwa", "rasuwa", "rasuwa", "rasuwa", "rupandehi", "sankhuwasabha", "sankhuwasabha", "sarlahi", "sindhuli", "sindhuli", "sindhuli", "sindhupalchok", "sindhupalchok", "sindhupalchok", "siraha", "solukhumbu", "solukhumbu", "solukhumbu", "solukhumbu", "sunsari", "sunsari", "syangja", "syangja", "syangja", "tbd", "tanahu", "tanahu", "tanahu", "taplejung", "taplejung", "udayapur", "udayapur", "udayapur", "lalitpur", "sindhuli", "sindhuli" ],
"Action.type": [ "housing", "health", "housing", "health", "housing", "housing", "housing", "finantial", "health", "housing", "finantial", "health", "housing", "finantial", "health", "housing", "housing", "finantial", "Labor", "health", "housing", "health", "housing", "finantial", "health", "housing", "finantial", "health", "housing", "health", "housing", "housing", "housing", "finantial", "health", "housing", "health", "finantial", "health", "housing", "finantial", "health", "housing", "finantial", "health", "housing", "finantial", "health", "housing", "health", "housing", "finantial", "health", "housing", "housing", "health", "housing", "health", "housing", "health", "housing", "finantial", "Labor", "health", "housing", "finantial", "health", "housing", "health", "housing", "health", "housing", "health", "housing", "housing", "finantial", "health", "housing", "finantial", "Labor", "health", "housing", "housing", "health", "housing", "housing", "finantial", "health", "housing", "finantial", "health", "housing", "health", "finantial", "Labor", "health", "housing", "health", "housing", "finantial", "health", "housing", "health", "finantial", "health", "housing", "health", "housing", "finantial", "health", "housing", "housing", "health", "housing" ],
"total": [ 2, 1, 1, 2, 21, 2, 1, 13, 28, 107, 1, 2, 4, 1, 2, 7, 1, 55, 2, 126, 348, 1, 2, 92, 153, 416, 53, 157, 631, 2, 3, 1, 1, 19, 207, 389, 1, 10, 8, 5, 29, 90, 280, 1, 67, 69, 49, 71, 274, 25, 202, 58, 45, 80, 1, 2, 1, 1, 3, 7, 21, 68, 2, 118, 198, 1, 94, 105, 2, 4, 1, 20, 8, 7, 1, 75, 90, 153, 4, 1, 180, 309, 1, 1, 1, 1, 38, 59, 140, 87, 369, 937, 1, 1, 10, 66, 79, 2, 1, 1, 7, 4, 2, 5, 7, 6, 27, 2, 1, 6, 8, 1, 1, 1 ] 
}''')

class DataLocator:
    """ Inteface / Abstract Class concept for readability. """

    def find(self, image):
        # explicitly set it up so this can't be called directly
        raise NotImplementedError('Exception raised, DataLocator is supposed to be an interface / abstract class!')

class DataLocatorFeedback(DataLocator):
    ''' Locates Feedback Information'''
    
    data = '''{"kavrepalanchok": ["27.58333", "85.66667"], "dolakha": ["27.68027", "86.0701"], 
    "lalitpur": ["27.67658", "85.31417"], "dhading": ["27.86424", "84.9283"], 
    "bhaktapur": ["27.67298", "85.43005"], "ramechhap": ["27.32207", "86.05913"], 
    "makwanpur": ["27.41667", "85.25"], "kathmandu": ["27.70169", "85.3206"], 
    "nuwakot": ["28", "83.83333"], "sindhuli": ["27.2799", "85.98421"], 
    "rasuwa": ["27.08617", "86.42758"], "okhaldhunga": ["27.31032", "86.50502"], 
    "gorkha": ["28.00242", "84.62009"], "sindhupalchowk": [0, 0]}'''
    
    def find(self, coord):
		dname = Coord2District().get_district(coord)[0][0]
		district_coordinates = districts[dname]
		q = request.args.get("q")
		t = feedback.return_jsonlist(dname,district_coordinates[0],district_coordinates[1],q)
		d = '''[
		{
			"Name":"%s",
			"lat":"%s",
			"long":"%s",
			"tag": "%s",
			"type": "feedback",
			"d":{
		            "#1 Concern": %s,
		            "#1 Concern percentage":%s
		        }
		}
		]''' % (dname,district_coordinates[0],district_coordinates[1],q,t[0],t[1])    
		return d


class DataLocatorBaseline(DataLocator):
    ''' Locates images in database. '''
    def find(self, image):
        #in reality, query database for image path
        return ["Baseline Data"]

class Coord2District():
	def get_district(self,coord):
		return district_distance.order_districts(coord[0],coord[1],districts)

class DataLocatorHumanitarian(DataLocator):
    ''' Locates images in database. '''
    def find(self, coord):
		dname = Coord2District().get_district(coord)[0][0]
		district_coordinates = districts[dname]
		q = request.args.get("q")
		
		t = []
		k = humanitarian.keys()[0]
		
		for i in xrange(0,len(humanitarian[k])):
			if (humanitarian['District'][i] == dname) & (humanitarian['Action.type'][i] == q ):
				t.append(humanitarian['total'][i])
				break
		s = sum([float(humanitarian['total'][i]) for i in xrange(0,len(humanitarian[k])) if humanitarian['District'][i] == dname]) 	
		s = (t[0] / s) * 100
		t.append("%f.2"%s)	
		
		d = '''[
		{
			"Name":"%s",
			"lat":"%s",
			"long":"%s",
			"tag": "%s",
			"type": "humanitarian",
			"d":{
		            "#1 Concern": %s,
		            "#1 Concern percentage":%s
		        }
		}
		]''' % (dname,district_coordinates[0],district_coordinates[1],q,t[0],t[1])
		return d

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):

	locators = [DataLocatorHumanitarian,DataLocatorBaseline,DataLocatorFeedback]
	coord = (request.args.get('x'),request.args.get('y'))
	d = "{}"
	if request.args.get("type") == "feedback":
		d = locators[-1]()	
	elif request.args.get("type") == "baseline":
		d = locators[1]()
	elif request.args.get("type") == "humanitarian":
		d = locators[0]()
	else:
		return d
	return d.find(coord)

if __name__ == '__main__':
	app.run(debug=True)
	coord = (27.69169, 85.3206)
	locators = [DataLocatorHumanitarian,DataLocatorBaseline,DataLocatorFeedback]
	res =[]
	for l in locators:
		loc = l()
		res.append( loc.find(coord)	)

	print res




