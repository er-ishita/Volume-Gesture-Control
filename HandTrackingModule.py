import cv2
import mediapipe as mp
import time

class HandDetector:
    def __init__(self,mode=False,maxHands=2, detectCon=0.5, trackCon=0.5):
        self.mode=mode
        self.maxHands=2
        self.detectCon=detectCon
        self.results=None
        self.trackCon=trackCon

        self.mpDraw=mp.solutions.drawing_utils
        self.mpHand=mp.solutions.hands
        self.hand=self.mpHand.Hands()

    
    def findHands(self,img, draw=True):
        imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results=self.hand.process(imgRGB)
        # print(self.results.multi_hand_landmarks)
        
        if self.results.multi_hand_landmarks:
            w,h,_=img.shape
            for handlm in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handlm, self.mpHand.HAND_CONNECTIONS)

        return img
    
    def findPosition(self,img,handNo=0, draw=True):
        # imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        lmList=[]

        if self.results and self.results.multi_hand_landmarks:
            hand=self.results.multi_hand_landmarks[handNo]
            h,w,_=img.shape
            for id,lm in enumerate(hand.landmark):
                cx,cy=int(lm.x*w),int(lm.y*h)
                if draw:
                    cv2.circle(img,(cx,cy),10,(0,255,0),cv2.FILLED)
                lmList.append([id,cx,cy])
        return lmList

def main():
    cam=cv2.VideoCapture(0)
    ptime=0
    detect=HandDetector()

    while True: 
        suc,img=cam.read()
        
        if not suc:
            print("Image not captured")
            break

        img=cv2.flip(img,1)
        img=detect.findHands(img)
        lm=detect.findPosition(img)

        ctime=time.time()
        fps=int(1/(ctime-ptime))
        ptime=ctime

        if len(lm)!=0:
            print(lm[4])
        
        cv2.putText(img,f'FPS: {fps}', (10,70),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),2)
        cv2.imshow("WebCam",img)

        if cv2.waitKey(1) & 0xff==ord('q'):
            print("Quitting")
            break
    
    cam.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
    main()