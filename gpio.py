
import RPi.GPIO as GPIO
import time
import config as c

def add_pulse(channel):
    c.LAST_PULSE = time.time()
    c.PULSES += 1
#    print('add pulse', time.time()-c.LAST_PULSE)
#    print('new last pulse', c.LAST_PULSE,'last coin',c.LAST_COIN)

def cleanup():
    print('cleaning up')
    GPIO.cleanup()

def count_pulses():
    if (time.time() - c.LAST_PULSE < 0.3):
        pass
    elif (time.time() - c.LAST_PULSE > 0.3) and (c.PULSES > 0):
        print('time: ', (time.time() - c.LAST_PULSE))
        print('pulses: ', c.PULSES)
        print((time.time() - c.LAST_PULSE > 0.3), (c.PULSES > 0))
        if c.PULSES == 1:
            c.COINS += 0.5
            c.COINS_INSERTED.append(0.5)
            print('\n0.5,',c.COINS, c.COINS_INSERTED)
        elif c.PULSES == 2:
            c.COINS += 1
            c.COINS_INSERTED.append(1)
            print('\n1',c.COINS,c.COINS_INSERTED)
        elif c.PULSES == 3:
            c.COINS += 2
            c.COINS_INSERTED.append(2)
            print('\n2',c.COINS, c.COINS_INSERTED)
        elif c.PULSES == 4:
            c.COINS += 5
            c.COINS_INSERTED.append(5)
            print('\n5',c.COINS, c.COINS_INSERTED)
        elif c.PULSES == 5:
            c.COINS += 10
            c.COINS_INSERTED.append(10)
            print('\n10',c.COINS, c.COINS_INSERTED)
        elif c.PULSES >=5:
            print('bigger than error')
        c.PULSES = 0
        c.LAST_COIN = time.asctime()


# initiate raspi gpios
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(6, GPIO.FALLING, callback=add_pulse)

# test time
#while True:
#    count_pulses()
