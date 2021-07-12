import pigpio


def servo_start(gpio, werte):
    werte.servo = pigpio.pi()
    werte.servo.set_PWM_frequency(gpio, 400)
    werte.servo.set_PWM_dutycycle(gpio, 127)


def servo_search(gpio, werte):
    if werte.servo_search_clockwise:
        werte.servopos +=2
        werte.servo.set_PWM_dutycycle(gpio, werte.servopos)
        if werte.servopos >= 167:
            werte.servo_search_clockwise = False
    else:
        werte.servopos -=2
        werte.servo.set_PWM_dutycycle(gpio, werte.servopos)
        if werte.servopos <= 87:
            werte.servo_search_clockwise = True


def servo_control(gpio, werte):
    k_p = 0.0045
    k_i = 0.00001
    k_d = 0.002

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

