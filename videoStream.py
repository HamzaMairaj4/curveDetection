from centerLine import *
from curveCenter import *
import cv2 as cv
import numpy as np

def videoStreamProcess(port):
    #open video
    capture = cv.VideoCapture(port)


    while True:
        #capture frame
        ret, frame = capture.read()
        h, w, channel=frame.shape
        quarH = h//4
        quarW = w//4
        upperLeft = (quarW,quarH)
        bottomRight = (3*quarW,3*quarH)

        #if frame is read correctly ret is True

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # mask
        rectFrame = frame[upperLeft[1]: bottomRight[1], upperLeft[0]:bottomRight[0]]

        #process frame
        procFrame = rectFrame
        try:
            procFrame, nayFrame = curveCenter(rectFrame)
        except:
            procFrame=curveCenter(rectFrame)


        # replace mask
        try:
            frame[upperLeft[1]: bottomRight[1], upperLeft[0]:bottomRight[0]]=procFrame
            rect = cv.rectangle(frame, upperLeft, bottomRight, (0, 0, 0), 5)

        except:
            pass

        #Display the resulting frame
        cv.imshow('frame', frame)
        try:
            cv.imshow('nay',nayFrame)
        except:
            pass
        if cv.waitKey(1) == ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()




