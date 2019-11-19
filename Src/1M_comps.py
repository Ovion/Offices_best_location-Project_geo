import pymongo
import fn_mongo as fm 

def load_dollar():
    print('\n Loading 1 million dollar companies ...\n')
    mills_coll = fm.connect_collection('companies', 'companies')

    comps_dollar = list(mills_coll.find({'raised_dollar':{'$gte':1000000}}))

    m_coll = fm.connect_collection('companies', '1_Million')

    m_coll.insert_many(comps_dollar)
    print('Done')


