from assimilate import *
import cv2 as cv
import numpy as np

#Process frame & detect curves
def midnight(frame):
    while True:
        # Establish grayscale frame and run thru canny detector (30, 150)
        grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        grayFrame = cv.GaussianBlur(grayFrame, (9, 9), 0)

        nayFrame = cv.Canny(grayFrame,30,150)

        # use findContours to detect curves (straight lines are curves, too!)
        contours, hier = cv.findContours(nayFrame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

        # attempt to process contours
        try:
            # sort contours to get the biggest and smallest curves (opposite sides of the two curves on frame, allows us to work around edge detection)
            contourSort = min(contours, key=lambda c: cv.contourArea(c)), max(contours, key=lambda c: cv.contourArea(c))

            # if no contours, skip frame
            if contours is None:
                print("Hough Line Transform Failed! Skipping Frame...")
                break

            # If contours, draw each detected contours, but then draw the mean line between the edge contours
            else:
                #Draw contours
                for contour in contours:
                    cv.drawContours(frame,[contour],-1,(0,0,255),4)

                #draw middle contour
                cv.polylines(frame,[np.array(assimilate(contourSort))],False,(255,0,0),4)

            break

        # if contours can't be processed for any reason, skip frame
        except:
            print("Transform Failed! Skipping Frame...")
            break

    # return processed frame,
    return frame, nayFrame