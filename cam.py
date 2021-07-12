from Values import Values
from servo import *
import cv2
import numpy as np
import time


def cam(gpio_servo, werte):
    cap = cv2.VideoCapture(0)
    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
    arucoParams = cv2.aruco.DetectorParameters_create()

    servo_start(gpio_servo, werte)

    while not werte.stop:
        # Bild aufnehmen
        ret, image = cap.read()

        # Marker Detektion durchführen
        (corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)

        if len(corners) > 0:
            ids = ids.flatten()

            for (markerCorner, markerID) in zip(corners, ids):
                if markerID == 0:
                    werte.marker_detected = True
                    corners = markerCorner.reshape((4, 2))
                    (topLeft, topRight, bottomRight, bottomLeft) = corners

                    x = int((topLeft[0] + bottomRight[0]) / 2.0)
                    y = int((topLeft[1] + bottomRight[1]) / 2.0)

                    w = int(np.sqrt((topRight[0] - topLeft[0]) ** 2 + (topRight[1] - topLeft[1]) ** 2))
                    h = int(np.sqrt((bottomLeft[0] - topLeft[0]) ** 2 + (bottomLeft[1] - topLeft[1]) ** 2))

                    werte.cam_pos = [x, y, w, h]

                    # Berechnung von Parametern für PID-Steuerung
                    x = x - 320
                    t = time.time()

                    integral = werte.cam[4] + x

                    # [x_1, x_0, t_1, t_0, sum(x)]
                    werte.cam = [x, werte.cam[0], t, werte.cam[2], integral]

                    # Servo
                    servo_control(gpio_servo, werte)


        else:
            werte.marker_detected = False

            # wenn gewünscht Servo rotieren, bis Marker gefunden
            if werte.search_for_marker:
                if time.time() - werte.cam[2] > 5:
                    servo_search(gpio_servo, werte)

        # wenn gewünscht Marker anzeigen
        if werte.showMarker:
            show_marker(image, werte)


def show_marker(image, werte):
    if werte.marker_detected:
        x, y = werte.cam_pos[:2]
        cv2.circle(image, (x, y), 4, (0, 255, 255), -1)
        cv2.putText(image, "Abstand Mitte: " + str(x - 320), (x, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255),
                    2)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    werte.image = image

if __name__ == "__main__":
    w = Values()
    cam(12, w)
