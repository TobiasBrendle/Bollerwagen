from servo import servo_start
import time
from Values import Values


def servo_run(gpio, werte):
    servo_start(gpio, werte)
    while True:
        #     werte.servo.set_PWM_dutycycle(gpio, werte.servopos)
        werte.servo.set_PWM_dutycycle(gpio, 100)
        time.sleep(3)
        werte.servo.set_PWM_dutycycle(gpio, 200)
        time.sleep(3)


if __name__ == "__main__":
    w = Values()
    servo_run(21, w)
