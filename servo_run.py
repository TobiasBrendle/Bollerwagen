from servo import servo_start
import time


def servo_run(gpio, werte):
    servo_start(gpio, werte)
    while True:
    #     werte.servo.set_PWM_dutycycle(gpio, werte.servopos)
        werte.servo.set_PWM_dutycycle(gpio, 100)
        time.sleep(3)
        werte.servo.set_PWM_dutycycle(gpio, 200)
        time.sleep(3)

