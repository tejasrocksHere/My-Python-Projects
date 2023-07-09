import cv2
import numpy as np
import os
import HandTrackingModule as htm

folderPath = "Header"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
detector = htm.handDetector(detectionCon=0.85)

for imPath in myList:
    image = cv2.imread(os.path.join(folderPath, imPath))
    overlayList.append(image)
print(len(overlayList))

header = overlayList[0]
header_height, header_width, _ = header.shape

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 728)

fingers = []  # Initialize fingers variable

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flip the frame horizontally

    # Find hand landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # Tip of index and middle finger
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        fingers = detector.fingersUp()
        print(fingers)

    # Check which fingers are up
    # If selection mode, two fingers are up, then select
    if len(fingers)>=3 and fingers[1] and fingers[2]:
        cv2.rectangle(img,(x1,y1-25),(x2,y2+25),(255,0,0),cv2.FILLED)
        print("Selection mode")
        if y1<125:
            if 250<x1<450:
                header=overlayList[0]
            elif 550<x1<750:
                header=overlayList[1]
            elif 800<x1<950:
                header=overlayList[2]
            elif 1050<x1<1200:
                header=overlayList[3]


    # If index finger is up, draw
    if len(fingers)>=2 and fingers[1] and not fingers[2]:
        cv2.circle(img,(x1,y1),15,(255,255,0),cv2.FILLED)
        print("Drawing mode")

    img_height, img_width, _ = img.shape
    header_resized = cv2.resize(header, (img_width, header_height))
    img[0:header_height, 0:img_width] = header_resized
    cv2.imshow("img", img)

    if cv2.waitKey(1) == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
