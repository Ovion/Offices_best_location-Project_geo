import pandas as pd
import pymongo
import numpy as np
import data_mongo as dm 

starbucks = pd.read_csv('../DB/starbucks.csv', usecols = [0, 4, 5, 11, 12])

starbucks = starbucks[starbucks.Longitude.apply(lambda x: type(x) in [int, np.int64, float, np.float64])]
starbucks = starbucks[starbucks.Latitude.apply(lambda x: type(x) in [int, np.int64, float, np.float64])]

starbucks['Localization']=np.vectorize(dm.geopoint)(starbucks['Longitude'], starbucks['Latitude'])

sbux_coll = dm.connect_collection('companies', 'starbucks')

sbux_coll.insert_many(starbucks.to_dict('record'))

# sbux_coll.delete_many({'$or':[{"Latitude":{'$eq':None}},{"Longitude":{'$eq':None}}]})

sbux_coll.delete_one({"Street Address":"23 & 23-1, Yoido-Dong, Yongdongpo-Gu, 1F, #101"})

sbux_coll.create_index ([('Localization', pymongo.GEOSPHERE)])






