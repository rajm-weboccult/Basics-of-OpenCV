import cv2

# Load image
image = cv2.imread('/home/wot-raj/image_processing_code/tiger.jpeg')

# Brighten by adding 50 to each pixel
brightened_image = cv2.add(image, 50)

# Darken by subtracting 50 from each pixel
darkened_image = cv2.subtract(image, 50)

# Display results
cv2.imshow('Brightened Image', brightened_image)
cv2.imshow('Darkened Image', darkened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()