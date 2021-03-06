# communication with the DeLight wallet
# to read atm devault wallet and send bought amount to client
# for readability I define commands for os as a string
# before calling

import os
import json
import config as c

def start_daemon():
    print('Starting daemon.')
    cmd = 'DeLight/delight daemon start'
    os.system(cmd)

def stop_daemon():
    print('Stopping daemon')
    cmd = 'DeLight/delight daemon stop'
    os.system(cmd)

def load_wallet(path_to_wallet):
    print('Loading wallet...')
    cmd = f'DeLight/delight -v daemon load_wallet -w {path_to_wallet}'
    output = os.popen(cmd).read()

def get_balance(path_to_wallet):
    load_wallet(path_to_wallet)
    print('getting balance')
    cmd = f'DeLight/delight -v getbalance -w {path_to_wallet}'
    balance_data = os.popen(cmd).read()
    # use json to convert str to dict and get balance
    # and make sure atm balance is updated
    confirmed_balance = float(json.loads(balance_data)['confirmed'])
    print(confirmed_balance)
    if len(json.loads(balance_data)) > 1:
        unconfirmed_balance = float(json.loads(balance_data)['unconfirmed'])
        print(unconfirmed_balance)
        if unconfirmed_balance < 0:
            return int(confirmed_balance + unconfirmed_balance)
    return int(confirmed_balance )##round(confirmed_balance, 0)

def deposit(address, amount, path_to_wallet):
    print('Beginning deposit')
    # the wallet can only handle 3 decimals or it breaks
    try:
        amount = int(amount) ##float(amount)
        print('amount: ', amount)
        # Set fee_per_kb and confirmed_only to make sure tx goes to mempool
        feecmd = './DeLight/delight -v setconfig fee_per_kb ' + str(c.TX_FEE_PER_KB)
        print(feecmd,os.popen(feecmd).read())
        confirmed_cmd = './DeLight/delight -v setconfig confirmed_only true'
        print(confirmed_cmd,os.popen(confirmed_cmd).read())
        load_wallet(path_to_wallet)
        ## make tx  - Removed fees and set fee above instead
        txcmd = f'./DeLight/delight payto -v -w {path_to_wallet} {address} {amount}'
        # set true to avoid error when converting data to dict, can be anything
        true = True
        tx_data = os.popen(txcmd).read()
        # use json to convert str to dict
        hex = json.loads(tx_data)['hex']
        print(hex)
        broadcast_cmd = f'DeLight/delight -v broadcast {hex}'
        tx = os.popen(broadcast_cmd).read()
        tx_id = json.loads(tx)[1]
        print(tx_id)
    except ValueError as e:
        tx_id = e
    return tx_id
