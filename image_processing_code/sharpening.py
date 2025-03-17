import cv2
import numpy as np

# Load image
image = cv2.imread('/home/wot-raj/image_processing_code/tiger.jpeg')

# Define a sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

# Apply sharpening
sharpened_image = cv2.filter2D(image, -1, kernel)

# Display result
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()