import cv2

# Load image
image = cv2.imread('/home/wot-raj/image_processing_code/tiger.jpeg')
height, width = image.shape[:2]

# Rotate 90 degrees clockwise
center = (width // 2, height // 2)
M = cv2.getRotationMatrix2D(center, -90, 1)
rotated_image = cv2.warpAffine(image, M, (width, height))

# Horizontal flip
flipped_image = cv2.flip(image, 1)

# Display results
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Flipped Image', flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()