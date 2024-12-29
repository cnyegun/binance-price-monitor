import requests
import json  

# ====================
# CONSTANT DEFINITIONS
# ====================
TOKEN_LIST = ['BTC', 'ETH', 'W', 'JUP', 'SEI', 'JTO', 'SUI', 'STRK', 'ZK', 'ENA', 'PEPE', 'DOGE']
PAIR_SYMBOL = 'USDT'

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

def getPrice():
    getAPI = "https://data-api.binance.vision/api/v3/ticker/price?symbols=" + concatSymbols()
    response = requests.get(getAPI)
    if response.status_code != 200: 
        print('GET failed')
        return
    response = response.json()
    for pair in response:
        print(f"{pair['symbol'][:-4]}: ${round(float(pair['price']), 3)}")

# ====================
#       RUNNER 
# ====================
if __name__ == "__main__":
    getPrice()
