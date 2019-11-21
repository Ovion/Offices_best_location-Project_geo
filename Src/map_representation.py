import pandas as pd
import folium


def print_map(df):
    max_rank_office = df.iloc[df['total_rank'].idxmax()]['offices']
    lon = max_rank_office['longitude']
    lat = max_rank_office['latitude']
    city = max_rank_office['city']

    map_city = folium.Map(location=[lat, lon], zoom_start=12)
    return 0
