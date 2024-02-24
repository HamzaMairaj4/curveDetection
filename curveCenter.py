from alg1 import *
from curveDetection import *
import numpy as np

def curveCenter(frame):
   try:
      lineFrame,nayFrame=midnight(frame)

      return lineFrame, nayFrame
   except:
      lineFrame=midnight(frame)

      return lineFrame