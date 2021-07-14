from binance.client import Client
import config

client = Client(config.api_key, config.api_secret)

# info = client.get_symbol_info('BNBBTC')
# info = client.get_exchange_info()
info = client.get_account()

print(info)

# timez = info['timezone']
# timez = info['serverTime']
# print(timez)

for i in info:
    print(i)
