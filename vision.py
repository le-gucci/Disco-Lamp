import cv2 as cv
import numpy as np

camfeed = cv.VideoCapture(0)


while True:
    isTrue, frame = camfeed.read()



    ## create mask to find ir

    ## ir = cv.cvtColor(

    ## lower_bound
    ## upper_bound

    ## irmask = cv.inRange
    irmask = None


    contours, _ = cv.findContours(irmask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    irblob = max(contours, key = cv.contourArea)

    M = cv.moments(irblob)

    cx = M["m10"]/M["m00"]
    cy = M["m01"]/M["m00"]

    cv.circle(frame, (cx, cy), 5, (0, 255, 0), 2)


    cv.imshow(frame)