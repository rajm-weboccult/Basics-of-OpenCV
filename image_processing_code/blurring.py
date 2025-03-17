import cv2

# Load image
image = cv2.imread('/home/wot-raj/image_processing_code/tiger.jpeg')

# Averaging Blur
averaged_blur = cv2.blur(image, (5, 5))

# Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# Median Blur
median_blur = cv2.medianBlur(image, 5)

# Bilateral Filtering
bilateral_blur = cv2.bilateralFilter(image, 9, 75, 75)

# Display results
cv2.imshow('Averaged Blur', averaged_blur)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imshow('Median Blur', median_blur)
cv2.imshow('Bilateral Blur', bilateral_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()