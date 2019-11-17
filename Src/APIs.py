
import requests


def currency_api(curr):
    '''
    This function will return a .json with the exchange rates, from given currency to all other currencies they support
    '''
    url = f'https://api.exchangerate-api.com/v4/latest/{curr}'
    res = requests.get(url)
    data = res.json()
    return data










