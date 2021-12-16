# to import Client from binance
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

# to import time
import time

# to import pprint
from pprint import pprint

# to import configapi (save api key and secret key)
import configapi

api_key = configapi.api_key
api_secret = configapi.api_secret
client = Client(api_key, api_secret)

# *** give an example of solusdt in my binance portfolio ***

# example of limit buy order
'''

order = client.order_limit_buy(
    symbol='SOLUSDT',
    quantity=1,
    price='50')

pprint(order)

'''

# example of limit sell order
order = client.order_limit_sell(
    symbol='SOLUSDT',
    quantity=1,
    price='200')

pprint(order)

# example of cancle order 
'''

result = client.cancel_order(
    symbol='SOLUSDT',
    orderId=fill your order id)

print(result)

'''

# to check all orders
# orders = client.get_all_orders(symbol='SOLUSDT')
# print('ALL ORDER: ',orders)

# to check open orders
# orders = client.get_open_orders(symbol='SOLUSDT')
# print('ALL ORDER: ', orders)

# to check all of asset
#info = client.get_account()
# pprint(info)

# to get fees for all assets
# fees = client.get_trade_fee()
# pprint(fees)

# to check bids and asks at that time
# depth = client.get_order_book(symbol='SOLUSDT')
# pprint(depth)

# to show quantity, prices, and amount money of trading
# trades = client.get_recent_trades(symbol='SOLUSDT')
# pprint(trades)

# to show price of asset that you want to know every 2 seconds
'''

while True:
    prices = client.get_all_tickers()
    current_price = ''
    coin_name = 'SOLUSDT'
    for p in prices:
        if p['symbol'] == coin_name:
            current_price = p

    print(current_price)
    time.sleep(0.2)
    # {'symbol': 'SOLUSDT', 'price': '182.45000000'}
    
'''

###############
'''

# to import all function (*) from tkinter
from tkinter import *

# to import Client from binance
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

# to import pprint
from pprint import pprint

# to import time
import time

# to import configapi (save api key and secret key)
import configapi

api_key = configapi.api_key
api_secret = configapi.api_secret
client = Client(api_key, api_secret)

# to check asset balance (example of sol and usdt)
sol = client.get_asset_balance(asset='SOL')
usdt = client.get_asset_balance(asset='USDT')
# print('SOL:', sol)
# print('USDT:', usdt)

# to show the example of asset both in portfolio and locked order
text_sol = '{} : {} (In order: {}) '.format(sol['asset'],sol['free'],sol['locked'])
text_usdt = '{} : {} (In order: {}) '.format(usdt['asset'],usdt['free'],usdt['locked'])
alltext = text_sol + '\n' + text_usdt

# to create a function of UpdatePrice (show price of asset that you want to know every 2 seconds)
def UpdatePrice():
    prices = client.get_all_tickers()
    current_price = ''
    coin_name = 'SOLUSDT'
    for p in prices:
        if p['symbol'] == coin_name:
            current_price = p

    # print(current_price)
    time.sleep(0.2)
    # {'symbol': 'SOLUSDT', 'price': '182.45000000'}
    v_current.set('{} : {}'.format(current_price['symbol'], current_price['price']))
    # to call the callback function once after a delay milliseconds (ms) within Tkinter's mainloop
    R1.after(100, UpdatePrice)
    
###############

# to create Python Launcher
GUI = Tk()

# to create the size of Python Launcher
GUI.geometry('700x300')

# to name the Python Launcher
GUI.title('JNBOT Crypto Check')

# to create font in each line and place variable in mainloop
FONT1 = ('Angsana New',20)
FONT2 = ('Impact',30)
L = Label(GUI,text='Amount Money',font=FONT1)
L.pack()

# to create empty string and lend every text to the set of string
v_balance = StringVar()
v_balance.set(alltext)

BL = Label(GUI,textvariable= v_balance, font=FONT1,fg='green')
BL.pack()

v_current = StringVar()

R1 = Label(GUI,textvariable= v_current, font=FONT2)
R1.pack()

# to call function UpdatePrice
UpdatePrice()

# to call function GUI
GUI.mainloop()

'''
