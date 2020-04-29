import config as c
import time


## Calculates which coin is inserted. REALLY need to make sure
## that user recieves a warning when reaching max buy
def calc_coins(atm_balance):
    max_buy = float(atm_balance) - c.TX_FEE #
    price_with_fee = c.PRICE_WITH_FEE
    dvt_bought = round(sum(c.COINS_INSERTED) / price_with_fee, 3)

    if (time.time() - c.LAST_PULSE > 0.5) and (c.PULSES > 0):
        if c.PULSES == 1:
            c.COINS_INSERTED.append(0.5)
            c.LAST_COIN = time.time()
            dvt_bought = sum(c.COINS_INSERTED) / price_with_fee
            print('You bought ' + str(0.5 / price_with_fee) + ' DVT' +
                  ' with 0.5 MXN')
            print('In total ' + str(dvt_bought) + ' DVT' + ' with ' +
                  str(sum(c.COINS_INSERTED)) + ' ' + c.FIAT_PAIR.upper() + '\n')
            print(c.COINS_INSERTED)

        elif c.PULSES == 2:
            c.COINS_INSERTED.append(1)
            LAST_COIN = time.time()
            dvt_bought = sum(c.COINS_INSERTED) / price_with_fee
            print('You bought ' + str(1 / price_with_fee) + ' DVT' +
                  ' with 1 MXN')
            print('In total ' + str(dvt_bought) + ' DVT' + ' with ' +
                  str(sum(c.COINS_INSERTED)) + ' ' + c.FIAT_PAIR.upper() + '\n')
            print(c.COINS_INSERTED)

        elif c.PULSES == 3:
            c.COINS_INSERTED.append(2)
            LAST_COIN = time.time()
            dvt_bought = sum(c.COINS_INSERTED) / price_with_fee
            print('You bought ' + str(2 / price_with_fee) + ' DVT' +
                  ' with 2 MXN')
            print('In total ' + str(dvt_bought) + ' DVT' + ' with ' +
                  str(sum(c.COINS_INSERTED)) + ' ' + c.FIAT_PAIR.upper() + '\n')
            print(c.COINS_INSERTED)

        elif c.PULSES == 4:
            c.COINS_INSERTED.append(5)
            LAST_COIN = time.time()
            dvt_bought = sum(c.COINS_INSERTED) / price_with_fee
            print('You bought ' + str(5 / price_with_fee) + ' DVT' +
                  ' with 5 MXN')
            print('In total ' + str(dvt_bought) + 'DVT' + ' with ' +
                  str(sum(c.COINS_INSERTED)) + ' ' + c.FIAT_PAIR.upper() + '\n')
            print(c.COINS_INSERTED)

        elif c.PULSES == 5:
            c.COINS_INSERTED.append(10)
            LAST_COIN = time.time()
            dvt_bought = sum(c.COINS_INSERTED) / price_with_fee
            print('You bought ' + str(10 / price_with_fee) + ' with 10 MXN')
            print('In total ' + str(dvt_bought) + ' DVT' + ' with ' +
                  str(sum(c.COINS_INSERTED)) + ' ' + c.FIAT_PAIR.upper() + '\n')
            print(c.COINS_INSERTED)

        c.PULSES = 0
        c.LAST_PULSE = 0
        c.COINS = sum(c.COINS_INSERTED)
