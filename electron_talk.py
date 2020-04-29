# communication with the delight/delight wallet
# to read atm devault wallet and send bought amount to client
# for readability I define commands for os as a string
# before calling

import os
import json
import config as c

def start_daemon():
    print('Starting daemon.')
    cmd = 'delight/delight daemon start'
    os.system(cmd)

def stop_daemon():
    print('Stopping daemon')
    cmd = 'delight/delight daemon stop'
    os.system(cmd)

def load_wallet(path_to_wallet):
    print('Loading wallet...')
    cmd = f'delight/delight -v daemon load_wallet -w {path_to_wallet}'
    output = os.popen(cmd).read()

def get_balance(path_to_wallet):
    start_daemon()
    load_wallet(path_to_wallet)
    print('getting balance')
    cmd = f'delight/delight -v getbalance -w {path_to_wallet}'
    balance_data = os.popen(cmd).read()
    stop_daemon()
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
        amount = float(amount) ##float(amount)
        print(amount)
        ## while fees are high to avoid dust
        amount_rounded = amount ##round(amount, 1)
        print(amount_rounded)

        ## make sure fee is set
        feecmd = './delight/delight -v setconfig fee_per_kb 1400000000'
        print('set fee 10',os.popen(feecmd).read())
        confirmed_cmd = './delight/delight -v setconfig confirmed_only true'
        print('set confirmed only ',os.popen(confirmed_cmd).read())
        #for test
        gfeecmd = './delight/delight -v getconfig fee_per_kb'
        print('check fee_per_kb: ', os.popen(gfeecmd).read())
        gconfirmed_cmd = './delight/delight -v getconfig confirmed_only'
        print('check confirmed_only: ', os.popen(gconfirmed_cmd).read())

        ## make tx  - Removed fees and set fee above instead
        txcmd = f' / {path_to_wallet} {address} {amount_rounded}'
        # set true to avoid error when converting data to dict, can be anything
        true = True
        tx_data = os.popen(txcmd).read()
        # use json to convert str to dict
        hex = json.loads(tx_data)['hex']
        print(hex)
        broadcast_cmd = f'delight/delight -v broadcast {hex}'
        tx = os.popen(broadcast_cmd).read()
        tx_id = json.loads(tx)[1]
        print(tx_id)
    except ValueError as e:
        tx_id = e
    return tx_id


def payout_to_client(address, amount, path_to_wallet):
    start_daemon()  # make sure daemon is running
    load_wallet(path_to_wallet)
    tx_id = deposit(address, amount, path_to_wallet)
    stop_daemon()
    return tx_id

# test
print(get_balance(c.ATM_WALLET))
print(payout_to_client('devault:qzkltxm33nye989chm34gkkeph48eq67euenxcvzq4', 42, c.ATM_WALLET))
