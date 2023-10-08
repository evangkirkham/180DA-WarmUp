# video capture with redbox and image tracking

import cv2 as cv
import numpy as np
from PIL import Image

def limits(color):
    #insert BGR values to convert into HSV
    c = np.uint8([[color]])
    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    # Give color range to find the upper and lower limits of the color you want to track
    lowerLim = hsvC[0][0][0] - 10, 100, 100
    upperLim = hsvC[0][0][0] + 10, 255, 255

    lowerLim = np.array(lowerLim, dtype = np.uint8)
    upperLim = np.array(upperLim, dtype = np.uint8)

    return lowerLim, upperLim

# initialize video capture
cap = cv.VideoCapture(0) 

# color we want to detect
blue = [255, 0, 0]

while True:
    ret, frame = cap.read()

    # adding color detection
    hsvImg = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lowerLimit, upperLimit = limits(color = blue)
    mask = cv.inRange(hsvImg, lowerLimit, upperLimit)

    # adding bounding box
    newmask = Image.fromarray(mask) # converts frame to be black and highlight in white all objects in frame of color specified to detect
    box = newmask.getbbox() # gets the box location of object

    # print box to frame
    if box is not None:
        x1, y1, x2, y2 = box
        frame = cv.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 5)


    cv.imshow('frame', frame)

    # close program when 'q' is pressed
    if cv.waitKey(1) & 0xff == ord('q'):
        break


cap.release()
cv.destroyAllWindows()