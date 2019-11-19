
from pymongo import MongoClient
import APIs

def connect_collection (database, collection):
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return coll


def count_values_subgroup (collection, group, subgroup):
    '''This function its like value_counts() in pandas, but count elements of a subgroup '''
    dicti = {}
    for coll in collection:
        for gr in coll[group]:
            dicti[gr[subgroup]]= dicti.get(gr[subgroup],0)+1
    sort_dicti = sorted(dicti.items(), key=lambda kv: kv[1], reverse=True)        
    return sort_dicti

def get_raised_dollar (company, exchange):
    '''Given a company and a dictionary of currency exchange rates returns the total amount '''
    dollars = 0
    try:
        for gr in company['funding_rounds']:
            if (gr['raised_currency_code'] in exchange['rates']) and (gr['raised_amount'] != None):
                dollars += gr['raised_amount']*exchange['rates'][gr['raised_currency_code']]
    except:
        company['funding_rounds'] = None
    return dollars

def get_location(company):

    lon = company['offices']['longitude']
    lat = company['offices']['latitude']
    loc = {
        'type':"Point",
        'coordinates': [float(lon), float(lat)]
    }
    return loc

def geopoint(lon, lat): 
    return {"type": "Point", "coordinates": [lon,lat]}



