import cv2
import numpy as np

# Load image
image = cv2.imread('/home/wot-raj/image_processing_code/tiger.jpeg')
height, width = image.shape[:2]

# Define translation matrix
tx, ty = 50, 30  # Move 50 pixels right and 30 pixels down
M = np.float32([[1, 0, tx], [0, 1, ty]])
translated_image = cv2.warpAffine(image, M, (width, height))

# Display result
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()