import cv2
import numpy as np

def empty(_):
    pass

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 18, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Saturation Min", "TrackBars", 55, 255, empty)
cv2.createTrackbar("Saturation Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Value Min", "TrackBars", 70, 255, empty)
cv2.createTrackbar("Value Max", "TrackBars", 299, 255, empty)

while True:
    success, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Saturation Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Saturation Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Value Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Value Max", "TrackBars")

    lower = (h_min, s_min, v_min)
    upper = (h_max, s_max, v_max)
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    stacked_frames = np.hstack((img, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR), result))
    cv2.imshow("Frames", stacked_frames)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
