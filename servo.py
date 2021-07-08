import RPi.GPIO as GPIO
import time
import pigpio


def servo_start(gpio, werte):
    pi = pigpio.pi()
    pi.set_PWM_frequency(gpio, 400)
    werte.servo = pi


def servo_control(gpio, werte):
    k_p = 0.004
    k_i = 0.000001
    k_d = 0.001

    x_pos = werte.cam[0]
    P = - x_pos * k_p  # P Anteil der Steuerung

    d = werte.cam
    dx = d[0] - d[1]
    dt = d[2] - d[3]
    D = - k_d * dx / dt  # D Anteil der Steuerung

    I = - k_i * werte.cam[4]

    PID = P + I + D
    werte.servopos += PID

    werte.servo.set_PWM_dutycycle(gpio, werte.servopos)

