import math
import cv2
import HandTrackingModule as htm
import numpy as np
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Audio stuff
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
print(minVol, maxVol)

volume.SetMasterVolumeLevel(0, None)

cap = cv2.VideoCapture(0)

wCam, hCam = 640, 480
cap.set(3, wCam)
cap.set(4, hCam)
volBar=400
volper=0

pTime = 0
detector = htm.handDetector(detectionCon=0.7)
vol = 0
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(img, (x1, y1), 10, (250, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (250, 0, 0), cv2.FILLED)
        cv2.circle(img, (cx, cy), 10, (250, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 24, 23), 2)

        length = math.hypot(x2 - x1, y2 - y1)
        print(length)
#converting to
        vol = np.interp(length, [50, 270], [minVol, maxVol])
        volBar=np.interp(length,[50,290],[400,150])
        volper=np.interp(length,[50,280],[0,100])
        print(vol)
        cv2.putText(img, str(int(volper)) + "%", (10, 170), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx, cy), 10, (0, 250, 0), cv2.FILLED)



    cv2.rectangle(img, (58, 158), (85, 400), (0, 250, 0), 3)
    cv2.rectangle(img,(58, int(volBar)), (85, 400), (0, 250, 0), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("img", img)
    cv2.waitKey(1)
