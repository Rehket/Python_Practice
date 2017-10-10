from cv2 import *
import numpy as np
from matplotlib import pyplot as plt





# Read Image
img = cv2.imread('images/00742_941201_fa.jpeg')

edge_threshold_low = 175
edge_threshold_high = 200

myEdges = cv2.Canny(img, edge_threshold_low, edge_threshold_high)


hist, bins = np.histogram(img.flatten(), 256, [0, 256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(), 256, [0, 256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf', 'histogram'), loc = 'upper left')
plt.show()


cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

normalizedImage = cdf[img]

myEdges2 = cv2.Canny(img, edge_threshold_low, edge_threshold_high)

# Display Image
cv2.imshow('image', img)
cv2.imshow('edges', myEdges)
cv2.imshow('norm', normalizedImage)
cv2.imshow('norm_Edges', myEdges2)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Applying Grayscale filter to image
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Saving filtered image to new file
# cv2.imwrite('graytest.jpg',gray)