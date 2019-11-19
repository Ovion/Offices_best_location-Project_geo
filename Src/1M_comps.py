import pymongo
import data_mongo as dm 

mills_coll = dm.connect_collection('companies', 'companies')

comps_dollar = list(mills_coll.find({'raised_dollar':{'$gte':1000000}}))

m_coll = dm.connect_collection('companies', '1_Million')

m_coll.insert_many(comps_dollar)


