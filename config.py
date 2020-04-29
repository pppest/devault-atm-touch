#from kivy.properties import StringProperty, NumericProperty

# for fetching price from coingecko
COIN = "devault"
FIAT_PAIR = "mxn"
DECIMALS = 3 # DeVaul wallet doesnt like txs with more decimals result is bad
PRICE_WITH_FEE = 0 ## set by coingecko.py

# atm specific
ATM_FEE = 1   # in percent
ATM_WALLET = '/home/pi/.delight/wallets/ATM_WALLET'
TX_FEE = 0  ##set to 0 becasei of trouble w new high fees

# use USB or GPIO(raspi) not implemented yet
#INPUT = 'GPIO'

# if using usb encoder
# Bus 001 Device 010: ID 0079:0006 DragonRise Inc. PC TWIN SHOCK Gamepad
#USB_VENDOR_ID = 0x0079
#USB_PRODUCT_ID = 0x0006

# kivy vars coin pulses counter
BG_IMAGES = []
BG_IMAGE = ''

PULSES = 0
LAST_PULSE = 0.0
LAST_COIN = 0.0
COINS = 0.0
COINS_INSERTED = []
MAXED_OUT = False

TIMEOUT = 30
