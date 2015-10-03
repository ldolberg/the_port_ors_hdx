import pandas as pd
import json

# -- open 'Nepal_F_Tagged.csv'
new_df = pd.read_csv('../data/Nepal/Nepal_F_Tagged.csv')

def total_percent_from_district_tag(district, tag, df):
    total = df[(df['District']==district)&(df['Tag']==tag)]['Count'].sum()
    surveyed_ppl_from_district = df[df['District']==district]['Count'].sum()
    percentage = total/surveyed_ppl_from_district
    return total, percentage

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
