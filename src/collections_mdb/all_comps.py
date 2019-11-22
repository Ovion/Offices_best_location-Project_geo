from pymongo import MongoClient
import pymongo
import functions.apis as api
import functions.fn_mongo as fm
import json
import os


def load_all():

    # import collection to pymongo
    bashCommand = 'mongoimport --db companies --collection companies --file ../dbs/companies.json'
    try:
        print('Importing collection to mongoDB ...')
        os.system(bashCommand)
        print('Done')
    except:
        pass

    print('\n Loading all companies ...\n')

    exchange = api.currency_api('USD')
    '''
    exchange = {'rates':{
                    'USD': 1,
                    'EUR': 0.906638,
                    'JPY': 108.679651,
                    'GBP': 0.776193,
                    'CAD': 1.323993,
                    'SEK': 9.667363}}
    '''
    # Conexion
    comps_coll = fm.connect_collection('companies', 'companies')

    # Borrar las que hayan quebrado
    comps_coll.delete_many({'deadpooled_year': {'$gte': 0}})

    # Borrar las que no tengan oficina
    comps_coll.delete_many({'offices': {'$eq': []}})

    # Hacer lista para actualizar
    comps_dollar = list(comps_coll.find({'deadpooled_year': None}))

    # Actualización de los datos para ver la cantidad en dolares
    for comp in comps_dollar:
        value_dollar = {
            "$set": {'raised_dollar': fm.get_raised_dollar(comp, exchange)}}
        comps_coll.update_one(comp, value_dollar)

    # Por cada oficina, crear un nuevo campo
    unpack = [{'$unwind': '$offices'}, {
        '$project': {'_id': 0}}, {'$out': 'companies'}]
    comps_coll.aggregate(unpack)

    # Borrar aquellas sin coordenadas
    comps_coll.delete_many({'$or': [{"offices.latitude": {'$eq': None}}, {
                           "offices.longitude": {'$eq': None}}]})

    # Borrar gilipolleces
    comps_coll.update_many({}, {'$unset': {'permalink': 1, 'crunchbase_url': 1, 'homepage_url': 1, 'blog_url': 1,
                                           'blog_feed_url': 1, 'twitter_username': 1, 'founded_month': 1, 'founded_day': 1,
                                           'deadpooled_year': 1, 'deadpooled_month': 1, 'deadpooled_day': 1, 'deadpooled_url': 1,
                                           'tag_list': 1, 'alias_list': 1, 'email_address': 1, 'phone_number': 1, 'created_at': 1,
                                           'updated_at': 1, 'overview': 1, 'image': 1, 'products': 1, 'relationships': 1, 'competitions': 1,
                                           'providerships': 1, 'milestones': 1, 'ipo': 1, 'video_embeds': 1, 'screenshots': 1, 'external_links': 1,
                                           'partners': 1, 'acquisition': 1, 'acquisitions': 1, 'investments': 1}})

    # lista para las localizaciones
    comps_loc = list(comps_coll.find())

    # poner las localizaciones en el formato requerido
    for comp in comps_loc:
        value_loc = {'$set': {'location': fm.get_location(comp)}}
        comps_coll.update_one(comp, value_loc)

    comps_coll.create_index([("location", pymongo.GEOSPHERE)])

    comps_coll.delete_one({'$and': [{"offices.city": 'Chicago'}, {
                          "location.coordinates": {'$lte': -120}}]})
    comps_coll.delete_one({'$and': [{"offices.city": 'Atlanta'}, {
                          "location.coordinates": {'$lte': -120}}]})
    comps_coll.delete_one({'$and': [{"offices.city": 'New York City'}, {
                          "location.coordinates": {'$lte': -120}}]})

    print('Done')
