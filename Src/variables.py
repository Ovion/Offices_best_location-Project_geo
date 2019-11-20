
def get_variables_perefence_1 (pref_1):

    query1 = {'raised_dollar':{'$gte':1000000}}
    query2 = {"$or": [
                {"category_code": "design"},
                {"category_code": "web"}, 
                {"category_code": "software"}, 
                {"category_code": "music"}, 
                {"category_code": "mobile"}, 
                {"category_code": "hardware"},   
                {"category_code": "network_hosting"} ,   
                {"category_code": "photo_video"}   
                ]}
    query3 = {'founded_year':{'$gte':2004}}

    if pref_1 == '1':
        return query1
    elif pref_1 == '2':
        return query2
    else:
        return query3













