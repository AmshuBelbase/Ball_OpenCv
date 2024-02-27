import cv2

# Open video file
video = cv2.VideoCapture("video14.mp4")

frame_count = 0

# Read frames one by one
while True:
    success, frame = video.read()

    if not success:
        break

    frame_count += 1

print("FPS: ", frame_count)
