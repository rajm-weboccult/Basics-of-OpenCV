import cv2
import numpy as np

# Load image
image = cv2.imread('/home/wot-raj/image_processing_code/tiger.jpeg')

# Create a mask
mask = np.zeros(image.shape[:2], dtype=np.uint8)
mask[50:200, 100:300] = 255

# Apply bitwise AND
masked_image = cv2.bitwise_and(image, image, mask=mask)

# Display result
cv2.imshow('Masked Image', masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()