import cv2

# Load image in grayscale
image = cv2.imread('/home/wot-raj/image_processing_code/tiger.jpeg', cv2.IMREAD_GRAYSCALE)

# Simple Thresholding
_, simple_thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Display results
cv2.imshow('Simple Thresholding', simple_thresh)
cv2.imshow('Adaptive Thresholding', adaptive_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()