import cv2 as cv
import numpy as np

camfeed = cv.VideoCapture(0)

while True:
    isTrue, frame = camfeed.read()

    print(isTrue)

    ir = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_bound = np.array([130, 50, 50])
    upper_bound = np.array([180, 255, 255])

    irmask = cv.inRange(ir, lower_bound, upper_bound)

    contours, _ = cv.findContours(irmask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        irblob = max(contours, key = cv.contourArea)

        cv.drawContours(frame, [irblob], 0, (0, 0, 0), 1)

        M = cv.moments(irblob)

        if M["m00"] != 0:
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])

            cv.circle(frame, (cx, cy), 5, (0, 255, 0), 2)
            print(cx, cy)


    cv.imshow("view", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()