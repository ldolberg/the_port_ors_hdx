import pandas as pd
import json


def return_jsonlist(district,lat,lon,tag):
    json_list = []
    # -- open 'Nepal_F_Tagged.csv'
    df = pd.read_csv('../../data/Nepal/Nepal_F_Tagged.csv')
    return total_percent_from_district_tag(district, tag, df)
    # -- get district from order_districts
    # -- use get_coordinates(district) to get lat, lon
    # -- get tag from query       

    # -- add entry in json-compatible format:


def total_percent_from_district_tag(district, tag, df):
    total = df[(df['District']==district)&(df['Tag']==tag)]['Count'].sum()
    surveyed_ppl_from_district = df[df['District']==district]['Count'].sum()
    percentage = total/max(surveyed_ppl_from_district,1)
    return total, percentage
