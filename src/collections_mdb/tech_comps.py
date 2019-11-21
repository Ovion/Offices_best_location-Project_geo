
import pymongo
import functions.fn_mongo as fm


def load_tech():
    print('\n Loading tech companies ...\n')
    t_coll = fm.connect_collection('companies', 'companies')

    comps_tech = list(t_coll.find({"$or": [
        {"category_code": "design"},
        {"category_code": "web"},
        {"category_code": "software"},
        {"category_code": "music"},
        {"category_code": "mobile"},
        {"category_code": "hardware"},
        {"category_code": "network_hosting"},
        {"category_code": "photo_video"}
    ]}))

    tech_coll = fm.connect_collection('companies', 'tech')

    tech_coll.insert_many(comps_tech)
    print('Done')
