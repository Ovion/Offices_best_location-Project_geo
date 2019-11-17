
from pymongo import MongoClient

def connect_collection (database, collection):
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll


def count_values_subgroup (collection, group, subgroup):
    '''This function its like value_counts() in pandas, but count elements of a subgroup '''
    dicti = {}
    for coll in collection:
        for gr in coll[group]:
            dicti[gr[subgroup]]= dicti.get(gr[subgroup],0)+1
    sort_dicti = sorted(dicti.items(), key=lambda kv: kv[1], reverse=True)        
    return dicti

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

def get_set_location(company, collection):
    indx = 0
    try:
        for gr in company['offices']:
            if (gr['longitude']!= None) and (gr['latitude']!= None):
                long = gr['longitude']
                lat = gr['latitude']
                loc = {
                    'type':'Point',
                    'coordinates':[float(long), float(lat)]
                }
                value = {"$set": {f"location {indx}": loc}}
                collection.update_one(company, value)
                indx +=1
    except:
        company['offices'] = None



