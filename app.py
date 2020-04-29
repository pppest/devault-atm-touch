
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
#from kivy.core.audio import SoundLoader

# import atm modules
import config as c
import coingecko as gecko
import gpio
import qr
import coinslot
import delight

# import other stuff
import time
import os

## Initiate wallet and get atm balance_data
delight.start_daemon()
balance = delight.get_balance(c.ATM_WALLET)


class StartScreen(Screen):
    pass


class BuyScreen(Screen):
    def goto_start_screen(self,dt):
        self.manager.current = 'start'


class CheckoutScreen(BuyScreen):
    # def goto_start_screen(self,dt):
    #     self.manager.current = 'start'
    pass


class Atm(ScreenManager):
    pass


class AtmApp(App):
    bg_images = os.listdir('images/bg_images/')
    start_image = StringProperty('images/Dstartscreen1.png')
    popup_text = StringProperty()
    time = StringProperty()
    rl_time = NumericProperty()
    start_time = 0.0
    atm_balance = NumericProperty(balance)
    coins_str = StringProperty()
    dvt_bought = NumericProperty()
    dvt_bought_str = StringProperty()
    client_address = StringProperty('No address! Scan your wallet QR!')
    client_qr = StringProperty('images/transparent.png')

 #   sound = SoundLoader.load('sounds/coin1.mp3')
 #   if sound:
 #       print("Sound found at %s" % sound.source)
 #       print("Sound is %.3f seconds" % sound.length)
 #       sound.play()

    def is_dvt_address(self, address, *args):
        return 'devault:' in address

    def has_address(self, *args):
        if not self.is_dvt_address(self.client_address):
            self.root.ids.qr.trigger_action()

    def get_qr(self, *args):
        if not self.is_dvt_address(self.client_address):
            self.client_address = qr.read_qr_code()
            self.client_qr = qr.generate_qr_code(self.client_address)
            self.start_time = self.rl_time

    def gen_qr(self, *args):
        return qr.generate_qr_code(*args)

    def cleanup_gpio(*args):
        return gpio.cleanup()

    def rotate_bg_image(self, *args):
        self.bg_images = [self.bg_images[(i + 1) % len(self.bg_images)] for i, x in enumerate(self.bg_images)]
        self.start_image = 'images/bg_images/' + self.bg_images[0]

    def update(self, *args):
        self.time = str(time.asctime())
        self.rl_time = time.time()

        if self.coins_str != str(c.COINS):
            self.coins_str = str(c.COINS)
            self.start_time = self.rl_time
#            self.sound.play()

        coinslot.calc_coins(balance)
        self.dvt_bought = c.COINS/c.PRICE_WITH_FEE
        self.dvt_bought_str = str(round(c.COINS/c.PRICE_WITH_FEE, 3))

        # deposit if timeout and dvt bought and wallet scanned
        # clean up later
        if self.root.current == 'buy':
            #print(self.root.current)
            if (self.rl_time - self.start_time >= c.TIMEOUT):
                print('TIMEOUT')
                if (self.dvt_bought > 0):
                    print('dvt bought')
                    if self.is_dvt_address(self.client_address):
                        print('is dvt addy start deposit')
                        self.root.current = 'checkout'
                        self.start_time = self.rl_time
                    else:
                        print('dvt bought no wallet trigger scan')
                        self.root.ids.qr.trigger_action()
                        self.start_time = self.rl_time
                else:
                    print('no dvt no wallet go to start')
                    self.root.current = 'start'
                    self.start_time = self.rl_time

    def build(self):
        Clock.schedule_interval(self.update, 0.1)
        return Atm()

if __name__ == "__main__":
    AtmApp().run()
    stop_daemon()
