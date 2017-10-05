from cv2 import *
import numpy as np


# Read Image
img = cv2.imread('images/feret_face_front.jpg')

myEdges = cv2.Canny(img, 75, 200)

# Display Image
cv2.imshow('image', img)
cv2.imshow('edges', myEdges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Applying Grayscale filter to image
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Saving filtered image to new file
# cv2.imwrite('graytest.jpg',gray)