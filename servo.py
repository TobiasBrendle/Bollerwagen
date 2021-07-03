import RPi.GPIO as GPIO
import time


def servo_start(GPIO_SERVO, werte):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_SERVO, GPIO.OUT)

    p = GPIO.PWM(GPIO_SERVO, 50)
    servo_pos = 7.5
    p.start(servo_pos)
    time.sleep(0.1)
    werte.servo = p


def servo_control(werte):
    k_p = 0.0005
    k_d = 0.00003

    x_pos = werte.cam[0]
    P = - x_pos * k_p   #P Anteil der Steuerung

    d = werte.cam
    dx_dt = d[0] - d[1] / (d[2] - d[3])
    D = dx_dt*k_d       #D Anteil der Steuerung

    PD = P + D
    werte.servopos += PD

    werte.servo.ChangeDutyCycle(werte.servopos)
