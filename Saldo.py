from binance.client import Client
import os
import config

client = Client(config.api_key, config.api_secret)

print(client.get_asset_balance(asset='BTC'))