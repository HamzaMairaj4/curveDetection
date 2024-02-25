from curveDetection import *


def curveCenter(frame):
   # attempt to process canny frame as well as contours
   try:
      lineFrame,nayFrame=midnight(frame)

      return lineFrame, nayFrame

   # if not, return raw frame for display
   except:
      lineFrame=midnight(frame)

      return lineFrame