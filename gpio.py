
import RPi.GPIO as GPIO
import time
import config as c


def add_pulse(channel):
    c.LAST_PULSE = time.time()
    c.PULSES += 1

def cleanup():
    print('cleaning up')
    GPIO.cleanup()

def initiate_gpio():
    GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(6, GPIO.FALLING, callback=add_pulse)
