
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
        if (yes_or_no == 'y') or (yes_or_no == 'n'):
            break
    
    if yes_or_no == 'y':
        ac.load_all()

    # Display menu preferences
    pref_1 = input ('Enter your first preference by the number: ')
    lst_pref = [1,2,3]
    while pref_1 not in lst_pref:
        pref_1 = input ('Please enter only a number between 1 and 3: ')
        if pref_1 in lst_pref:
            break

    comps_coll = fm.connect_collection('companies', 'companies')
    companies = comps_coll.find()
    df_comps = pd.DataFrame(companies)
    print('Getting all locations')
    lst_loc = [df_comps.location[e] for e in range(len(df_comps))]

    query1 = vble.get_variables_perefence (pref_1)
    df_comps = fm.rank (comps_coll, df_comps, query1, lst_loc, 1)


    # Display menu preferences
    pref_2 = input ('Enter your second preference by the number: ')
    while (pref_2 not in lst_pref) and (pref_2 == pref_1):
        pref_2 = input ('Please enter only a number between 1 and 3 and not the previuos one: ')
        if (pref_2 in lst_pref) and (pref_2 != pref_1):
            break

    query2 = vble.get_variables_perefence (pref_2)
    df_comps = fm.rank (comps_coll, df_comps, query2, lst_loc, 2)






if __name__ == '__main__':
    main()