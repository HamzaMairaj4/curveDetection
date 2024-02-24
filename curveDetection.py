import cv2 as cv
import numpy as np
from alg1 import *

def midnight(frame):
   while True:
       grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

       grayFrame = cv.GaussianBlur(grayFrame, (5, 5), 0)

       nayFrame = cv.Canny(grayFrame,70,120,apertureSize=3)

       contours = cv.findContours(nayFrame, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
       print(contours)
       print(type(contours))

       if contours is None:
           print("Hough Line Transform Failed! Skipping Frame...")
           break
       else:
           cv.drawContours(frame,contours[0],-1,(0,255,0),3)

       print(contours)

       return frame, nayFrame
