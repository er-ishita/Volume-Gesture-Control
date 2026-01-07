import cv2
import numpy as np
import time
import HandTrackingModule as htm
import math

#must do- "pip install pycaw"
from pycaw.pycaw import AudioUtilities


device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
ptime=0

#here 0 is for webcam, change to 1 for external device webcam
cam=cv2.VideoCapture(0)
detect=htm.HandDetector()

volumeRange=volume.GetVolumeRange()
# print(volumeRange)==(-63.5, 0.0, 0.5)
minVol=volumeRange[0]
maxVol=volumeRange[1]

print("Press 'q' at anytime to close")

while True:

    suc, img=cam.read()

    if not suc:
        print("NO CAMERA DETECTED")
        break
    
    img=cv2.flip(img,1)

    ctime=time.time()
    fps=int(1/(ctime-ptime))
    ptime=ctime

    img=detect.findHands(img)
    lmlist=detect.findPosition(img,draw=False)

    if len(lmlist)!=0:
        x1,y1=lmlist[4][1],lmlist[4][2]
        x2,y2=lmlist[8][1],lmlist[8][2]
        
        cx,cy=(x1+x2)//2,(y1+y2)//2

        cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

        cv2.circle(img, (x1,y1),10,(255,0,255),cv2.FILLED)
        cv2.circle(img, (x2,y2),10,(255,0,255),cv2.FILLED)
        cv2.line(img, (x1,y1),(x2,y2),(255,0,255),3)

        length=math.hypot(x2-x1,y2-y1)

        #myscale= 20-200
        if length<20:
            cv2.circle(img,(cx,cy),15,(0,255,0),cv2.FILLED)

        if length>200:
            cv2.circle(img,(cx,cy),15,(255,0,0),cv2.FILLED)
            cv2.line(img, (x1,y1),(x2,y2),(255,0,0),4)

        vol=np.interp(length,[20,200],[minVol,maxVol])
        volume.SetMasterVolumeLevel(vol, None)

    cv2.putText(img,f'FPS: {fps}',(10,70),1,cv2.FONT_HERSHEY_COMPLEX,(255,0,0),3)
    cv2.imshow("Volume Controller",img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()