import os
from flask import Flask
from flask import request
from flask import jsonify


from flask import Flask
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
	    	res += l.find(coords)	

    return res

if __name__ == '__main__':
    app.run()



class DataLocator:
    """ Inteface / Abstract Class concept for readability. """

    def find(self, image):
        # explicitly set it up so this can't be called directly
        raise NotImplementedError('Exception raised, DataLocator is supposed to be an interface / abstract class!')

class DataLocatorFeedback(DataLocator):
    ''' Locates Feedback Information'''

    def find(self, image):
        # in reality, query Flickr API for image path
        return ["Feedback Data"]


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
        