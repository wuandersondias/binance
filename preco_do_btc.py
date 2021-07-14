from binance.client import Client
import config

client = Client(config.api_key, config.api_secret)

preco_btc = client.get_symbol_ticker(symbol="BTCUSDT")
preco_btc_real = client.get_symbol_ticker(symbol="BTCBRL")
print("Preço do Bitcoin em Dolar, ",preco_btc)
print("Preço do Bitcoin em Real, ",preco_btc_real)