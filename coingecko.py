import requests
import json
import sys
import time
import config as c


def get_price(coin, pair):
    api = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={pair}"
    print('Getting price...')
    request = requests.get(api)
    json_data = json.loads(request.text)
    coin_price = json_data[f'{coin}'][f'{pair}']
    return coin_price

## Fee in percentage, set in config
def price_with_fee(coin, pair, fee, decimals):
    price_with_fee = round(get_price(coin, pair) * (1 + fee / 100),
                           decimals)
    return price_with_fee
