import cv2
import numpy as np

image = np.zeros((300, 300, 3), dtype="uint8")

# Change a pixel to red
image[100, 100] = [255, 0, 0]

cv2.imshow('Pixel Manipulation', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
