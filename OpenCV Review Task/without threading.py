import cv2
import numpy as np

RTSP_URLS=[
    "rtsp://admin:abc@1234@192.168.0.248:554/cam/realmonitor?channel=1&subtype=0",
    "rtsp://admin:abc@1234@192.168.0.248:554/cam/realmonitor?channel=2&subtype=0",
    "rtsp://admin:abc@1234@192.168.0.248:554/cam/realmonitor?channel=3&subtype=0"
]
#Video capture and previous frame
caps=[cv2.VideoCapture(url) for url in RTSP_URLS]
prev_frames = [None] * len(RTSP_URLS)

try:
    while True:
        grid=[]
        for i, cap in enumerate(caps):
            ret, frame=cap.read()
            if not ret:
                continue

            #Bilateral filter and cropping 10% from the bottom
            filtered=cv2.bilateralFilter(frame, 15, 95, 95)
            cropped=filtered[:int(filtered.shape[0] * 0.9), :]

            #Difference frame
            diff=(
                cv2.absdiff(cropped, prev_frames[i])
                if prev_frames[i] is not None
                else np.zeros_like(cropped)
            )
            prev_frames[i]=cropped.copy()

            #Resize frames for display and append to processed frames
            resized_bilateral,resized_diff=[cv2.resize(f,(400, 200)) for f in [cropped,diff]]
            grid.append(cv2.hconcat([resized_bilateral,resized_diff]))

        #Grid of processed frames
        if grid:
            cv2.imshow("Cameras",cv2.vconcat(grid))
            
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break  
finally:
    for cap in caps:
        cap.release()
    cv2.destroyAllWindows()
