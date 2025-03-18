import cv2
import numpy as np
import os

output_dir = "captured_images"

# Check if 5 frames are already captured
Curr_frames = [f for f in os.listdir(output_dir) if f.startswith("frame_") and f.endswith(".jpg")]
if len(Curr_frames) >= 5:
    print("Found 5 frames")
    frames = [cv2.imread(os.path.join(output_dir, f)) for f in sorted(Curr_frames)]
else:
    cap = cv2.VideoCapture(0) 
    if not cap.isOpened():
        print("Failed to open camera.")
    else:
        frames = []
        print("Capturing 5 frames")
        for i in range(5):
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture")
                break
            frames.append(frame)
            cv2.imwrite(os.path.join(output_dir, f"frame_{i+1}.jpg"), frame)
            cv2.imshow("Frame Capture", frame)
            if cv2.waitKey(5000) & 0xFF == ord('q'):  
                print("Exit")
                break
        cap.release()
        cv2.destroyAllWindows()

# Image transformation functions
def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

def rotate(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    return cv2.warpAffine(image, M, (w, h))

def scale(image, factor):
    return cv2.resize(image, None, fx=factor, fy=factor, interpolation=cv2.INTER_LINEAR)

def crop(image, x, y, w, h):
    return image[y:y+h, x:x+w]

# Apply transformations to each captured frame
manipulated_frames = []
for frame in frames:
    translated = translate(frame, 50, 50)
    rotated = rotate(frame, 45)
    scaled = scale(frame, 0.5)
    cropped = crop(frame, 50, 50, 200, 200)
    
    # Resize all images to the same size for consistency
    target_size = (frame.shape[1], frame.shape[0])
    translated_resized = cv2.resize(translated, target_size)
    rotated_resized = cv2.resize(rotated, target_size)
    scaled_resized = cv2.resize(scaled, target_size)
    cropped_resized = cv2.resize(cropped, target_size)
    
    # Create a horizontal combination (concatenating transformed frames horizontally)
    horizontal_combined = cv2.hconcat([translated_resized, rotated_resized, scaled_resized, cropped_resized])
    
    # Add the horizontally combined image to the list
    manipulated_frames.append(horizontal_combined)

# Combine all horizontal combined images vertically
final_image = cv2.vconcat(manipulated_frames)
small_final_image = cv2.resize(final_image, (int(final_image.shape[1] * 0.2), int(final_image.shape[0] * 0.2)))

# Save and display the final image
cv2.imwrite("output_combined_image.jpg", small_final_image)
cv2.imshow("Final Combined Image", small_final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
