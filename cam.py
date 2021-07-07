import time
from Values import Values

from servo import *

from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import numpy as np
import imutils


def cam(gpio, werte):
    cap = cv2.VideoCapture(0)
    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
    arucoParams = cv2.aruco.DetectorParameters_create()

    servo_start(gpio, werte)

    while True:
        marker_detected = False
        ret, image = cap.read()
        (corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)
        if len(corners) > 0:
            marker_detected = True
            # flatten the ArUco IDs list
            ids = ids.flatten()
            # loop over the detected ArUCo corners
            for (markerCorner, markerID) in zip(corners, ids):
                corners = markerCorner.reshape((4, 2))
            #    image = show_marker(corners, image)
            x = (corners[0, 0] + corners[2, 0]) / 2
            x = x - 320

            integral = werte.cam[4] + x
            werte.cam = [x, werte.cam[0], time.time(), werte.cam[2], integral]    #hier wird die Abweichung von x zur Mitte übergeben, zusätzlich die Zeit zum Bilden des Differentials, die 2 letzen Werte werden auch behalten
            servo_control(gpio, werte)

            werte.print_values()

      #  cv2.imshow("Image", image)
     #   cv2.waitKey(1)


def show_marker(corners, image):
    (topLeft, topRight, bottomRight, bottomLeft) = corners
    topRight = (int(topRight[0]), int(topRight[1]))
    bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
    bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
    bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
    topLeft = (int(topLeft[0]), int(topLeft[1]))

    cv2.line(image, topLeft, topRight, (0, 255, 0), 10)
    cv2.line(image, topRight, bottomRight, (0, 255, 0), 10)
    cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 10)
    cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 10)

    cX = int((topLeft[0] + bottomRight[0]) / 2.0)
    cY = int((topLeft[1] + bottomRight[1]) / 2.0)

    w = bottomRight[0] - bottomLeft[0]
    h = topLeft[1] - bottomLeft[1]

    cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)

    cv2.putText(image, str(cX) + " , " + str(cY),
                (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 0, 0), 2)
    return image


if __name__ == "__main__":
    w = Values()
    cam(21, w)
