import os
import config
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

client = Client(config.api_key, config.api_secret)

btc_price = {'error':False}

def btc_trade_history(msg):
    ''' define how to process incoming WebSocket messages '''
    if msg['e'] != 'error':
        print(msg['c'])
        btc_price['last'] = msg['c']
        btc_price['bid'] = msg['b']
        btc_price['last'] = msg['a']
    else:
        btc_price['error'] = True

# init and start the WebSocket
bsm = BinanceSocketManager(client)
conn_key = bsm.start_symbol_ticker_socket('BTCUSDT', btc_trade_history)
bsm.start()

# stop websocket
bsm.stop_socket(conn_key)

# properly terminate WebSocket
reactor.stop()