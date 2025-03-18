import cv2
import numpy as np

RTSP_URLS = [
    "rtsp://admin:abc@1234@192.168.0.248:554/cam/realmonitor?channel=1&subtype=0",
    "rtsp://admin:abc@1234@192.168.0.248:554/cam/realmonitor?channel=2&subtype=0",
    "rtsp://admin:abc@1234@192.168.0.248:554/cam/realmonitor?channel=3&subtype=0"
]
# Parameters for bilateral filter
bilateral= {"d": 15, "sigmaColor": 95, "sigmaSpace": 95}

# Initialize video captures and previous frames
caps = [cv2.VideoCapture(url) for url in RTSP_URLS]
previous_frames = [None] * len(RTSP_URLS)

#Loop for processing and displaying frames
while True:
    processed_frames = []

    for i, cap in enumerate(caps):
        ret, frame = cap.read()
        if not ret:
            continue 
        #Bilateral filter
        bilateral_frame = cv2.bilateralFilter(frame, **bilateral)

        #Cropped 10% from the bottom
        h,w = bilateral_frame.shape[:2]
        cropped_frame = bilateral_frame[:int(h*0.9), :]
        
        #Compute difference frame
        diff_frame = (
        cv2.absdiff(cropped_frame, previous_frames[i][:int(h*0.9), :])
        if previous_frames[i] is not None
        else np.zeros_like(cropped_frame)
    )
        #Update previous frame
        previous_frames[i] = frame

        #Resize frames to reduce display size
        resized_bilateral = cv2.resize(cropped_frame, (300,200))
        resized_diff = cv2.resize(diff_frame, (300,200))

        processed_frames.append(cv2.hconcat([resized_bilateral, resized_diff]))

    # All rows into a grid
    if processed_frames:
        grid = cv2.vconcat(processed_frames)
        cv2.imshow("RTSP Stream Processing",grid)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()