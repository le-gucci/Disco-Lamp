from picamera2 import Picamera2
import cv2

picam2 = Picamera2()

# Configure for preview
config = picam2.create_preview_configuration(
    main={"size": (640, 480)}
)

picam2.configure(config)
picam2.start()

while True:
    frame = picam2.capture_array()

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
picam2.stop()