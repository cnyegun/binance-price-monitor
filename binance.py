import requests
import json  
import time 
from plyer import notification



# ====================
# CONSTANT DEFINITIONS
# ====================
TOKEN_LIST = ['BTC', 'ETH', 'W', 'JUP', 'SEI', 'JTO', 'SUI', 'STRK', 'ZK', 'ENA']
PAIR_SYMBOL = 'USDT'
DELAY_TIME = 5*60 # Seconds
NOTICE_WHEN_DIFFER = 1 # Percent

# ====================
#   GLOBAL VARIABLES
# ====================
price_list = [] 

# ====================
# FUNCTION DEFINITIONS
# ====================
# NULL -> String
# produce symbols for getPrice() function, based on TOKEN_LIST and PAIR_SYNBOL (global)
def concatSymbols():
    symbols = '['
    for token in TOKEN_LIST:
        symbols += '"' + token + PAIR_SYMBOL + '"' + ','
    symbols = symbols[:-1]
    symbols += ']'
    return symbols

# NULL -> JSON 
def getPrice():
    getAPI = "https://data-api.binance.vision/api/v3/ticker/price?symbols=" + concatSymbols()
    response = requests.get(getAPI)
    if response.status_code != 200: notiErr('GET failed')
    return response.json()

# Float Float Float -> Notify
def priceNotify(symbol, pa, diff):
    notification.notify(
        title = "Price Changes",
        message = f"${symbol[:-4]}: {diff}% now {pa}",
        app_name = "Binance Price Monitoring")

# JSON -> Notify
def checkVotality(current_prices):
    for lp, cp in zip(price_list, current_prices):
        symbol = lp['symbol']
        price_before = float(lp['price'])
        price_after = float(cp['price'])
        diff = round((1 - price_after/price_before)*100, 2)
        if abs(diff) >= NOTICE_WHEN_DIFFER:
            priceNotify(symbol, price_after, diff)
def main():
    try:
        # Variables
        current_prices = []
        global price_list  
        # Function calls
        current_prices = getPrice()
        if price_list != None:
            checkVotality(current_prices)
        price_list = current_prices
    except Exception as e:
        print(e)


# ====================
#       RUNNER 
# ====================
if __name__ == "__main__":
    while True:
        main()
        time.sleep(DELAY_TIME)
