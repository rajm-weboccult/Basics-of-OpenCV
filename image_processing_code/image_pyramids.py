import cv2

# Load image
image = cv2.imread('/home/wot-raj/image_processing_code/tiger.jpeg')

# Downscale using Gaussian Pyramid
lower_res = cv2.pyrDown(image)

# Upscale back
higher_res = cv2.pyrUp(lower_res)

# Display results
cv2.imshow('Lower Resolution', lower_res)
cv2.imshow('Higher Resolution', higher_res)
cv2.waitKey(0)
cv2.destroyAllWindows()