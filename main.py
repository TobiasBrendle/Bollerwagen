import threading
from cam import *
from tof import *
from ultrasonic import *
from Values import Values
from gui import *

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set GPIO Pins
GPIO_TRIGGER = [22, 27, 20, 6, 5]
GPIO_ECHO = [2, 4, 21, 13, 26]

GPIO_SERVO = 12


def start(werte):
    t1 = threading.Thread(target=tof, args=(werte,))
    t2 = threading.Thread(target=ultrasonic, args=(GPIO_TRIGGER, GPIO_ECHO, werte))
    t3 = threading.Thread(target=cam, args=(GPIO_SERVO, werte))

    t1.start()
    t2.start()
    t3.start()


if __name__ == '__main__':
    werte = Values()
    start(werte)
    g = Gui(werte)
