import pymongo
import fn_mongo as fm 

def load_new():
    print('\n Loading new companies ...\n')
    news_coll = fm.connect_collection('companies', 'companies')

    comps_new = list(news_coll.find({'founded_year':{'$gte':2004}}))

    n_coll = fm.connect_collection('companies', 'newest')

    n_coll.insert_many(comps_new)
    print('Done')