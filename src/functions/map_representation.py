import pandas as pd
import folium
import functions.fn_mongo as fm
import functions.fn_menu as menu
from os import system


def print_map(df, the_city):
    max_rank_office = ''
    for e in df.offices:
        if e['city'] == the_city:
            max_rank_office = e
            break
    # max_rank_office = df.iloc[df['total_rank'].idxmax()]['offices']
    lon = max_rank_office['longitude']
    lat = max_rank_office['latitude']
    city = max_rank_office['city']

    menu.display_Mmap(city, lon, lat)

    dollar_coll = fm.connect_collection('companies', '1_Million')
    dollars = dollar_coll.find({"offices.city": city})
    new_coll = fm.connect_collection('companies', 'newest')
    news = new_coll.find({"offices.city": city})
    tech_coll = fm.connect_collection('companies', 'tech')
    techs = tech_coll.find({"offices.city": city})

    map_city = folium.Map(location=[lat, lon], zoom_start=17)

    for dollar in dollars:
        folium.Marker(dollar['location']['coordinates'][::-1],
                      radius=2,
                      icon=folium.Icon(icon='usd', color='green')).add_to(map_city)

    for new in news:
        if new not in dollars:
            folium.Marker(new['location']['coordinates'][::-1],
                          radius=2,
                          icon=folium.Icon(icon='flash', color='orange')).add_to(map_city)

    for tech in techs:
        if (tech not in dollars) and (tech not in news):
            folium.Marker(tech['location']['coordinates'][::-1],
                          radius=2,
                          icon=folium.Icon(icon='cog', color='red')).add_to(map_city)

    folium.Circle([lat, lon],
                  fill_color='#de2314', color='blue',
                  radius=300
                  ).add_to(map_city)

    folium.Marker([lat, lon],
                  radius=2,
                  icon=folium.Icon(icon='star-empty', color='blue')).add_to(map_city)

    map_city.save('../output/map_ubication.html')
    _ = system('google-chrome ../output/map_ubication.html')
