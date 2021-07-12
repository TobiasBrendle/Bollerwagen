import serial
import time


def tof(werte):
    ser = serial.Serial("/dev/ttyAMA0", 115200, timeout=1)
    while not werte.stop:
        time.sleep(0.1)
        count = ser.in_waiting
        if count > 8:
            recv = ser.read(9)
            ser.reset_input_buffer()

            if recv[0] == 0x59 and recv[1] == 0x59:
                distance = recv[2] + recv[3] * 256
                strength = recv[4] + recv[5] * 256
                ds = distance  # , strength
                werte.tof = ds
                ser.reset_input_buffer()
