import time


class Values:
    #hier sind alle Werte der Sensoren gespeichert
    def __init__(self):
        self.uso = [0, 0, 0, 0, 0]
        self.tof = 0
        self.cam = [0, 0, 0, time.time()]
        self.servo = None
        self.servopos = 7.5

    def refresh_uso(self, pos, value):
        self.uso[pos] = value

    def print_values(self):
        print(self.uso, self.tof)
