import pandas as pd
import json


def return_jsonlist(district,lat,lon,tag,json_list):
    # -- open 'Nepal_F_Tagged.csv'
    new_df = pd.read_csv('../data/Nepal/Nepal_F_Tagged.csv')
    total, percentage = total_percent_from_district_tag(district, tag, df)
    # -- get district from order_districts
    # -- use get_coordinates(district) to get lat, lon
    # -- get tag from query       

    # -- add entry in json-compatible format:
    json_list.append({"Name":district, "lat":lat, "long":lon, "tag": tag,"type": "feedback",
                      "d":{
                "#1 Concern": total,
                "#1 Concern percentage":percentage}
                      })
    return json_list

def total_percent_from_district_tag(district, tag, df):
    total = df[(df['District']==district)&(df['Tag']==tag)]['Count'].sum()
    surveyed_ppl_from_district = df[df['District']==district]['Count'].sum()
    percentage = total/surveyed_ppl_from_district
    return total, percentage

def slice_df(df, query={}): 
    # -- approach two (builds slicing vector, *then* applies it)
    # -- more efficient
    
    # I'm assuming query is a dictionary                                                                                                                                             
    # query = {'Tag':tag, 'District':district, 'Gender':gender, 'Ethnicity':ethnicity}
    # -- select fields s.t. the df has them
    valid_query_args = list(df.columns)
    ret = df.copy()
    
    for requirement, value in query.iteritems():
        if requirement in valid_query_args:
            if requirement != 'Tag':
                ret = ret[ret[requirement] == value] # slicing without Tag
     
     denominator = ret['Count'].sum()    
     ret = ret[ret['Tag'] == query['Tag']] # slicing with Tag
     numerator = ret['Count'].sum()                          
     total = numerator
     percentage = numerator/max(denominator,1)
     return total, percentage


    
               
    
