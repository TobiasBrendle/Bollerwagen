import time
import pigpio


class Values:
    # hier sind alle Werte der Sensoren gespeichert
    def __init__(self):

        self.uso = [0, 0, 0, 0, 0]
        self.tof = 0
        self.cam_pos = [0, 0, 0, 0]
        self.cam = [0, 0, time.time(), 0, 0]  # P-Wert, P-Wert_vorher, t, t_vorher, I-Wert
        self.servo = pigpio.pi()
        self.servopos = 127

        self.marker_detected = False
        self.showMarker = True      #GUI -> Radio Button um Bild einzuschalten
        self.image = 0              #GUI -> Bild mit markiertem Marker, zum Anzeigen in der GUI

        self.distance_setting = [200, 1]    #GUI -> Edit Field, um Einstellung für Abstand einzugeben (Gewünschter Abstand, stäke der Beschleunigung bei Abweichung)

        self.steer = 0

        self.search_for_marker = False  #GUI -> Radio Button um suchfunktion (radar) einzuschalten
        self.servo_search_clockwise = True

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

    def get_values(self):
        if self.marker_detected:
            x = abs(self.cam[0])
            if abs(x)<20:
                F = 500
                D = 9.7
                P=max(self.cam_pos[2:])
                d = F*D/P-self.tof
                if abs(d)<30:
                    value = True
                    msg = "Alles gut"
                    speed = self.get_speed()
                    self.steer = self.get_steer()
                else:
                    value = False
                    msg = "Tof nicht richtig ausgerichtet"
                    speed = 0
            else:
                value = False
                msg = "Kamera nicht richtig ausgerichtet"
                speed = 0
        else:
            value = False
            msg = "Marker nicht gefunden"
            speed = 0
        return self.steer, speed, value, msg

    def get_speed(self):
        d = self.tof
        offset, factor = self.distance_setting
        d = d - offset
        speed = d*abs(factor)
        if speed <= 0:
            speed = 0

        if speed >= 100:
            speed = 100

        return speed

    def get_steer(self):
        steer = self.servopos
        steer -= 128
        steer = steer*1.5
        if steer < -50:
            steer = -50
        if steer > 50:
            steer = 50
        return steer
