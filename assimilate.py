# detect center parallel contours
def assimilate(contours):
   # Make sure we have enough contours to process
   if len(contours) >= 2:
      # Which ever contour is smaller, thats how many points
      minLength = min(len(contours[0]), len(contours[1]))

      # List of points for the middle contour
      averagePoints = []

      for i in range(minLength):
         # For all points in the contours, find their middle coordinates and add them to the list of average points
         x_avg = int((contours[0][i][0][0] + contours[1][i][0][0]) / 2)
         y_avg = int((contours[0][i][0][1] + contours[1][i][0][1]) / 2)
         averagePoints.append((x_avg, y_avg))

      # Return the midline
      return averagePoints
   else:
      pass



