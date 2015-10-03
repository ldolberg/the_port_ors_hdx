import os
from flask import Flask
from flask import request
from flask import jsonify
import json
import random

from flask import Flask
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
    
    def find(self, image):
        # in reality, query Flickr API for image path
        return [random.choice([k for k, v in json.loads(self.data).iteritems()])]
        
        #return ["Feedback Data"]


class DataLocatorBaseline(DataLocator):
    ''' Locates images in database. '''
    def find(self, image):
        #in reality, query database for image path
        return ["Baseline Data"]


class DataLocatorHumanitarian(DataLocator):
    ''' Locates images in database. '''
    def find(self, image):
        #in reality, query database for image path
        return ["Humanitarian Data"]

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    
    locators = [DataLocatorHumanitarian,DataLocatorBaseline,DataLocatorFeedback]

    res = 'You want path: %s<br/>' % path
    res += "Your query string is %s<br/>" % request.query_string
    if request.args.get('x'):
    	coords = (request.args.get('x'),request.args.get('y'))
    	for l in locators:
    		loc = l()
	    	res += loc.find(coords)	

    return res

if __name__ == '__main__':
 locators = [DataLocatorHumanitarian,DataLocatorBaseline,DataLocatorFeedback]
 res = ""
 coords = (1.0,2.0)
 for l in locators:
	loc = l()
	res += "%s\n" % loc.find(coords)[0]	
print res



        