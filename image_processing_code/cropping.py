import cv2

# Load image
image = cv2.imread('/home/wot-raj/image_processing_code/tiger.jpeg')

# Crop a region
cropped_image = image[50:200, 100:300]  # y1:y2, x1:x2

# Display result
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()