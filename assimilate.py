from alg1 import *
import cv2 as cv
import numpy as np

#detect center parallel contours
def assimilate(frame, contours, hier):
   #convert contours to a list
   contList=list(contours)

   #sort contList based on contourArea
   contList.sort(key=cv.contourAreas())

   #Establish maximum curves
   john=contList[-1]
   jeff=contList[-2]

   print(john)
   print(jeff)