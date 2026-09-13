import cv2
from gpiozero import LED
import time

# LED connected to GPIO 17
led = LED(17)

# Initialize cameras
cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)
cam3 = cv2.VideoCapture(2)

# Capture images
ret1, img1 = cam1.read()
ret2, img2 = cam2.read()
ret3, img3 = cam3.read()

# Check whether all cameras captured successfully
if ret1 and ret2 and ret3:

    # Save images
    cv2.imwrite("camera1.jpg", img1)
    cv2.imwrite("camera2.jpg", img2)
    cv2.imwrite("camera3.jpg", img3)

    print("All 3 pictures captured!")

    # Flash LED
    led.on()
    time.sleep(0.5)
    led.off()

    print("LED flashed!")

else:
    print("Camera capture failed.")

# Release cameras
cam1.release()
cam2.release()
cam3.release()
