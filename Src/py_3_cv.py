from cv2 import *


# Read Image
img = cv2.imread('../images/feret_face_front_2.jpg')

edge_threshold_low = 175
edge_threshold_high = 200

myEdges = cv2.Canny(img, edge_threshold_low, edge_threshold_high)


myEdges2 = cv2.Canny(img, edge_threshold_low, edge_threshold_high)

# Display Image
cv2.imshow('image', img)
cv2.imshow('edges', cv2.invert(myEdges))


cv2.waitKey(0)
cv2.destroyAllWindows()


# Applying Grayscale filter to image
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Saving filtered image to new file
# cv2.imwrite('graytest.jpg',gray)