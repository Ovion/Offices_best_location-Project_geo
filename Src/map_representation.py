import pandas as pd
import folium
import fn_mongo as fm
from os import system


def print_map(df):
    max_rank_office = df.iloc[df['total_rank'].idxmax()]['offices']
    lon = max_rank_office['longitude']
    lat = max_rank_office['latitude']
    city = max_rank_office['city']

    dollar_coll = fm.connect_collection('companies', '1_Million')
    dollars = dollar_coll.find({"offices.city": city})
    new_coll = fm.connect_collection('companies', 'newest')
    news = new_coll.find({"offices.city": city})
    tech_coll = fm.connect_collection('companies', 'tech')
    techs = tech_coll.find({"offices.city": city})

    map_city = folium.Map(location=[lat, lon], zoom_start=12)
    for dollar in dollars:
        folium.Marker(dollar['location']['coordinates'][::-1],
                      radius=2,
                      icon=folium.Icon(icon='usd', color='green')).add_to(map_city)

    for new in news:
        folium.Marker(new['location']['coordinates'][::-1],
                      radius=2,
                      icon=folium.Icon(icon='flash', color='yellow')).add_to(map_city)

    for tech in techs:
        folium.Marker(tech['location']['coordinates'][::-1],
                      radius=2,
                      icon=folium.Icon(icon='cog', color='red')).add_to(map_city)

    map_city.save('../output/map_ubication.html')
    _ = system('firefox ../output/map_ubication.html')
