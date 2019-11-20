
from pymongo import MongoClient
import pandas as pd
import requests
import APIs
import fn_mongo as fm 
import all_comps as ac
import variables as vble


def main():
    # Display menu start
    # Display load data
    yes_or_no = input('Do you need to load data? [y/n]: ')
    while (yes_or_no != 'y') or (yes_or_no != 'n'):
        yes_or_no = input('Please enter a "y" or a "n" (without ""): ')
    
    if yes_or_no == 'y':
        ac.load_all()

    # Display menu preferences
    pref_1 = input ('Enter your first preference by the number: ')
    lst_pref = [1,2,3]
    while pref_1 not in lst_pref:
        pref_1 = input ('Please enter only a number between 1 and 3: ')

    comps_coll = fm.connect_collection('companies', 'companies')
    companies = comps_coll.find()
    df_comps = pd.DataFrame(companies)
    lst_loc = [df_comps.location[e] for e in range(len(df_comps))]

    radio = 5000
    query1 = vble.get_variables_perefence_1(pref_1)
    lst_num_offices = []

    for i in range(len(df_comps)):
        num_off = fm.find_offices_near(comps_coll, lst_loc[i], query1, radio)
        lst_num_offices.append(len(num_off))
        
    df_comps['number_offices_1'] = lst_num_offices
    
    df_comps['rank1'] = df_comps['number_offices_1'].rank(pct=True)





    # Display menu preferences
    pref_2 = input ('Enter your second preference by the number: ')
    while pref_2 not in lst_pref:
        pref_2 = input ('Please enter only a number between 1 and 3: ')







if __name__ == '__main__':
    main()