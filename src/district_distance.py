
import math
import operator
import json
from geopy.distance import great_circle


class Order_districts():
    
    def get_district_info():
        # -- get names and coordinates from csv file
        with open('coordinates.json') as coord_file:    
            district_dict = json.load(coord_file)
        return district_dict


    #get_district_info(); # test for json reading

    def distance(lat0, lon0, lat, lon):
        '''
        Calculates distance on Earth's surface in meters
        '''
        return great_circle((lat0,lon0), (lat,lon)).meters
    
    def e_distance(x,y,w,z): 
        '''
        Euclidean distance calculation for simple sorting purposes
        '''
        a = math.pow(x - w,2)
        b = math.pow(y - z,2)
        return math.sqrt(a+b)  

    def order_districts(lat0, lon0, district_dict):
        '''
        function that return a list of names of districts ordered by distance from the point (lat0,lon0) passed from map
        Inputs: 'lat0' = latitude of point at center of map
                'lon0' = longitude of point at center of map
                'district_dict' = dict of district names and (lat,lon) from function get_district_info()
        Outputs: df with district names ordered by distance, coordinates of district (lat,lon)
        '''
        distance_dict={}
        # -- loop thru entries in coord/name dictionary
        for key, value in district_dict.iteritems():
            lat = float(value[0]); lon = float(value[1]);
            # -- calculate coords in radians
            #Delta_lat = math.radians(lat0-lat) # latitudinal distance 
            #Delta_lon = math.radians(lon0-lon) # longitudinal distance
            #lat0 = math.radians(lat0) # convert to radians
            #lat = math.radians(lat)
            distance_dict[key] = distance(lat0, lon0, lat, lon)
    
        sorted_districts = sorted(distance_dict.items(), key=operator.itemgetter(1))

        return zip(*sorted_districts) 
