import cv2

# Load image
image = cv2.imread('/home/wot-raj/image_processing_code/tiger.jpeg')

# Resize to half the original size
resized_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display result
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()