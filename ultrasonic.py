import time
import RPi.GPIO as GPIO


def measurement(trigger, echo, sensornr, werte):
    GPIO.output(trigger, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.05)
    GPIO.output(trigger, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(echo) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(echo) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    # if distance > 10:
    werte.refresh_uso(sensornr, round(distance, 2))



def ultrasonic(GPIO_TRIGGER, GPIO_ECHO, werte):
    # set GPIO direction (IN / OUT)
    for i in GPIO_TRIGGER:
        GPIO.setup(i, GPIO.OUT)

    for i in GPIO_ECHO:
        GPIO.setup(i, GPIO.IN)

    while not werte.stop:
        for i in range(5):
            trigger = GPIO_TRIGGER[i]
            echo = GPIO_ECHO[i]
            measurement(trigger, echo, i, werte)