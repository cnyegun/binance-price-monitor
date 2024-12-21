# Binance Price Monitor

A Python script that monitors the prices of selected cryptocurrencies on Binance and sends desktop notifications when significant price changes occur.

## Features

- **Real-Time Monitoring**: Tracks prices of specified cryptocurrencies against USDT.
- **Customizable Alerts**: Notifies when the price difference exceeds a defined percentage.
- **Desktop Notifications**: Uses desktop notifications to alert you of price changes.
- **Configurable Parameters**: Easily adjust the list of tokens, alert thresholds, and update intervals.

## Default Tokens

- BTC
- ETH
- W
- JUP
- SEI
- JTO
- SUI
- STRK
- ZK
- ENA
- ... add your own token

## Requirements

- Python 3.x
- `requests` library
- `plyer` library

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/cnyegun/binance-price-monitor.git
   cd binance-price-monitor
   ```
2. **Install Dependencies**
   ```bash
   pip install requests plyer
   ```
## Configuration
The script can be configured by modifying the constants defined at the beginning of the script:
```python
# Token symbols to monitor
TOKEN_LIST = ['BTC', 'ETH', 'W', 'JUP', 'SEI', 'JTO', 'SUI', 'STRK', 'ZK', 'ENA']

# Trading pair
PAIR_SYMBOL = 'USDT'

# Delay between price checks (in seconds)
DELAY_TIME = 300  # 5 minutes

# Alert threshold percentage
NOTICE_WHEN_DIFFER = 5  # 5%
```
## Usage
Run the script using Python:
```bash
python binance.py
```
## Example Notification
```
Title: Price Changes
Message: $BTC: -5.00% now 30000
```

