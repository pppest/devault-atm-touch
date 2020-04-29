## Global vars and settings

## for fetching price from coingecko
COIN = "devault"
FIAT_PAIR = "mxn"
DECIMALS = 3 # DeLight doesnt like txs with more decimals result is bad
PRICE_WITH_FEE = 0 ## set by coingecko.py

# ATM specific
ATM_FEE = 1   # in percent
ATM_WALLET = '/home/pi/.delight/wallets/ATM_WALLET'
TX_FEE = 0  ##set to 0 becasei of trouble w new high fees
TIMEOUT = 30    # Screen timeout in secs
PULSES = 0
LAST_PULSE = 0.0
LAST_COIN = 0.0
COINS = 0.0
COINS_INSERTED = []
