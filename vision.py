import cv2 as cv
from picamera2 import Picamera2
import numpy as np
from motorControl import adjust ## moneyyyy

picam2 = Picamera2()

config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(config)
picam2.start()

#camfeed = cv.VideoCapture(0)

while True:
    frame = picam2.capture_array()
    #isTrue, frame = camfeed.read()
    w = frame.shape[1]
    h = frame.shape[0]

    cx = w//2
    cy = h//2

    cv.circle(frame, (cx, cy), 3, (255, 0, 0), 1)
    ##(B, G, R) = frame[cy, cx]
    ##rgb = [int(x) for x in (R, G, B)]

    (h, s, v) = cv.cvtColor(frame, cv.COLOR_BGR2HSV)[cy, cx]
    hsv = [int(x) for x in (h, s, v)]
    ##print(hsv)
    ##print(isTrue)

    ir = cv.cvtColor(frame, cv.COLOR_RGB2HSV)

    lower_bound = np.array([140, 220, 220])
    upper_bound = np.array([155, 255, 255])

    irmask = cv.inRange(ir, lower_bound, upper_bound)

    contours, _ = cv.findContours(irmask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        irblob = max(contours, key = cv.contourArea)

        cv.drawContours(frame, [irblob], 0, (0, 0, 0), 1)

        M = cv.moments(irblob)

        if M["m00"] != 0:
            tx = int(M["m10"]/M["m00"])
            ty = int(M["m01"]/M["m00"])

            cv.circle(frame, (tx, ty), 5, (0, 255, 0), 2)

            adjust(cx, cy, tx, ty)


    cv.imshow("view", frame)

    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
picam2.stop()