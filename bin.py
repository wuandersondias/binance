from binance.client import Client
import config

client = Client(config.api_key, config.api_secret)
print("Logged in")

# info = client.get_symbol_info('BNBBTC')
# info = client.get_exchange_info()
info = client.get_account()

print(info)

# timez = info['timezone']
# timez = info['serverTime']
# print(timez)

for i in info:
    print(i)


preco_btc = client.get_symbol_ticker(symbol="BTCUSDT")
preco_btc_real = client.get_symbol_ticker(symbol="BTCBRL")
print(preco_btc, preco_btc_real)