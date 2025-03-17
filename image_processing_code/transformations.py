import cv2
import numpy as np

# Load image
image = cv2.imread('/home/wot-raj/image_processing_code/tiger.jpeg')
height, width = image.shape[:2]

# Translation
tx, ty = 50, 30  # Shift right by 50 pixels, down by 30 pixels
M = np.float32([[1, 0, tx], [0, 1, ty]])
translated_image = cv2.warpAffine(image, M, (width, height))

# Rotation
center = (width // 2, height // 2)
angle = -45  # Rotate 45 degrees clockwise
scale = 1.0
M = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, M, (width, height))

# Display results
cv2.imshow('Translated Image', translated_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()