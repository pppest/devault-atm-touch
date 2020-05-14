
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

import time
import os

# ATM modules
import config as c
import coingecko as gecko
import gpio
import qr
import coinslot
import delight


### check if DeLight exists and downloads if not
print(os.popen('sh ./has_delight.sh').read())

## Start daemon, get ATM balance, DVT price and initiate raspi gpio
delight.start_daemon()
balance = delight.get_balance(c.ATM_WALLET)
c.PRICE_WITH_FEE =  gecko.price_with_fee(c.COIN, c.FIAT_PAIR, c.ATM_FEE, c.DECIMALS)

gpio.initiate_gpio()


class StartScreen(Screen):
    pass


class BuyScreen(Screen):
    def goto_start_screen(self,dt):
        self.manager.current = 'start'


class CheckoutScreen(BuyScreen):
    pass


class Atm(ScreenManager):
    pass


## The App class mainly updates properties of the kivy ATM
## the widgets are defined in atm.kv
class AtmApp(App):
    start_time = 0.0
    time = StringProperty()
    rl_time = NumericProperty()
    atm_balance = NumericProperty(balance)
    coins_str = StringProperty()
    dvt_bought = NumericProperty()
    dvt_bought_str = StringProperty()
    client_address = StringProperty('No address! Scan your wallet QR!')
    client_qr = StringProperty('images/transparent.png')
    popup_text = StringProperty()
    value_of_biggest_coin = c.biggest_coin * c.price_with_fee

    def is_dvt_address(self, address, *args):
        return 'devault:' in address

    def has_address(self, *args):
        if not self.is_dvt_address(self.client_address):
            self.root.ids.qr.trigger_action()

    def read_qr(self, *args):
        if not self.is_dvt_address(self.client_address):
            self.client_address = qr.read_qr_code()
            self.client_qr = qr.generate_qr_code(self.client_address)
            self.start_time = self.rl_time

    def gen_qr(self, *args):
        return qr.generate_qr_code(*args)

    def update(self, *args):
        self.time = str(time.asctime())
        self.rl_time = time.time()
        if self.coins_str != str(c.COINS):
            self.coins_str = str(c.COINS)
            self.start_time = self.rl_time
        coinslot.calc_coins(balance)
        self.dvt_bought = c.COINS/c.PRICE_WITH_FEE
        self.dvt_bought_str = str(round(c.COINS/c.PRICE_WITH_FEE, 3))

        # deposit if timeout and dvt bought and wallet scanned
        if self.root.current == 'buy':
            # show warning if atm_balance low
            if atm_balance <= 2 * value_of_biggest_coin:
                self.app.popup_text = 'WARNING! \n ATM balance low and ATM doesnt give back'
                self.root.Factory.MyPopup().open()
            
            if (self.rl_time - self.start_time >= c.TIMEOUT):
                print('TIMEOUT')
                if (self.dvt_bought > 0):
                    print('dvt bought', self.dvt_bought)
                    if self.is_dvt_address(self.client_address):
                        print('is dvt addy starting deposit')
                        self.root.current = 'checkout'
                        self.start_time = self.rl_time
                    else:
                        print('dvt bought, no wallet trigger scan')
                        self.root.ids.qr.trigger_action()
                        self.start_time = self.rl_time
                else:
                    print('no dvt, no wallet, go to start')
                    self.root.current = 'start'
                    self.start_time = self.rl_time

    def build(self):
        Clock.schedule_interval(self.update, 0.1)
        return Atm()

if __name__ == "__main__":
    AtmApp().run()
