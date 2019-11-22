
from pymongo import MongoClient
import pandas as pd
import requests
import functions.fn_mongo as fm
import functions.variables as vble
import functions.map_representation as mp
import functions.fn_menu as menu
import collections_mdb.all_comps as ac
import collections_mdb.million_comps as mc
import collections_mdb.new_comps as nc
import collections_mdb.tech_comps as tc


def main():
    # Display menu start
    # Display load data
    options = ['y', 'n']
    yes_or_no = str(input('Do you need to load data? [y/n]: '))
    while yes_or_no not in options:
        yes_or_no = input('Please enter a "y" or a "n" (without ""): ')
        if yes_or_no in options:
            break

    if yes_or_no == 'y':
        ac.load_all()
        mc.load_dollar()
        nc.load_new()
        tc.load_tech()

    menu.display_M1()
    pref_1 = str(input('Enter your first preference by the number: '))
    lst_pref = ['1', '2', '3']
    while pref_1 not in lst_pref:
        pref_1 = input('Please enter only a number between 1 and 3: ')
        if pref_1 in lst_pref:
            break

    comps_coll = fm.connect_collection('companies', 'companies')
    companies = comps_coll.find()
    df_comps = pd.DataFrame(companies)
    print('Getting all locations')
    lst_loc = [df_comps.location[e] for e in range(len(df_comps))]

    query1 = vble.get_variables_perefence(pref_1)
    df_comps = fm.rank(comps_coll, df_comps, query1, lst_loc, 1)

    menu.display_M2()
    pref_2 = str(input('Enter your second preference by the number: '))
    while (pref_2 not in lst_pref) and (pref_2 == pref_1):
        pref_2 = input(
            'Please enter only a number between 1 and 3 and not the previuos one: ')
        if (pref_2 in lst_pref) and (pref_2 != pref_1):
            break

    query2 = vble.get_variables_perefence(pref_2)
    df_comps = fm.rank(comps_coll, df_comps, query2, lst_loc, 2)

    # 3rd query
    prev_q = [query1, query2]
    pref_3 = 0
    for i in lst_pref:
        if str(i) not in prev_q:
            pref_3 = str(i)
    query3 = vble.get_variables_perefence(pref_3)
    df_comps = fm.rank(comps_coll, df_comps, query3, lst_loc, 3)

    # total rank
    df_comps['total_rank'] = df_comps.iloc[:, -3]*0.6 + \
        df_comps.iloc[:, -2]*0.3 + df_comps.iloc[:, -1]*0.1

# -------

    df_comps = df_comps.sort_values(by=['total_rank'], ascending=False)
    lst_cities = []
    for e in df_comps.offices:
        if e['city'] not in lst_cities:
            lst_cities.append(e['city'])
            if len(lst_cities) == 3:
                break

    menu.display_Mcity(lst_cities)

    the_city = str(input('Enter THE city: '))
    while the_city not in lst_cities:
        the_city = input('Please enter a valid city: ')
        if the_city in lst_cities:
            break

    max_rank_office = {}
    for e in df_comps.offices:
        if e['city'] == the_city:
            max_rank_office = e
            break
    lon_city = max_rank_office['longitude']
    lat_city = max_rank_office['latitude']

    mp.print_map(the_city, lon_city, lat_city)


if __name__ == '__main__':
    main()
