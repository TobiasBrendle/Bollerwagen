import threading
from cam import *
from tof import *
from ultrasonic import *
from servo import *
from servo_test import *
from Values import Values
from gui import *

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

# set GPIO Pins
GPIO_TRIGGER1 = 23
GPIO_ECHO1 = 24
GPIO_TRIGGER2 = 27
GPIO_ECHO2 = 22
#GPIO_TRIGGER3 = 
#GPIO_ECHO3 = 
#GPIO_TRIGGER4 = 
#GPIO_ECHO4 = 
#GPIO_TRIGGER5 = 
#GPIO_ECHO5 =

GPIO_SERVO = 21


if __name__ == '__main__':
    werte = Values()
    try:
        
        t0=threading.Thread(target=tof, args=(werte,))
        t1=threading.Thread(target=ultrasonic, args=(GPIO_TRIGGER1, GPIO_ECHO1, 1, werte))
        t2=threading.Thread(target=ultrasonic, args=(GPIO_TRIGGER2, GPIO_ECHO2, 2, werte))
 #       t3=threading.Thread(target=ultrasonic, args=(GPIO_TRIGGER3, GPIO_ECHO3, 3))
  #      t4=threading.Thread(target=ultrasonic, args=(GPIO_TRIGGER4, GPIO_ECHO4, 4))
   #     t5=threading.Thread(target=ultrasonic, args=(GPIO_TRIGGER5, GPIO_ECHO5, 5))
        t6=threading.Thread(target=cam, args=(GPIO_SERVO, werte))
      #  t7=threading.Thread(target=gui, args=(werte,))
      #  t8=threading.Thread(target=servo_run, args=(GPIO_SERVO, werte))
        t0.start()
        t1.start()
        t2.start()
 #       t3.start()
  #      t4.start()
   #     t5.start()
        t6.start()
      #  t7.start()
    #    t8.start()
        #t0.join()
        #t1.join()
        #t2.join()
 #       t3.join()
  #      t4.join()
   #     t5.join()
        #t6.join()
        g = Gui(werte)

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()