import time
import pigpio


class Values:
    # hier sind alle Werte der Sensoren gespeichert
    def __init__(self):
        self.uso = [0, 0, 0, 0, 0]
        self.tof = 0
        self.cam = [0, 0, time.time(), 0, 0]  # P-Wert, P-Wert_vorher, t, t_vorher, I-Wert
        self.servo = pigpio.pi()
        self.servopos = 150

    def refresh_uso(self, pos, value):
        self.uso[pos] = value

    def print_values(self):
        print(self.uso, self.tof, self.cam, self.servopos)

    def get_uso_color(self, n):
        a = self.uso[n]
        if a < 100:
            color = "red"
        elif a < 150:
            color = "orange"
        else:
            color = "green"
        return color
