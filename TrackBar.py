import cv2
import numpy as np

def fxn(x):
    print(x)

img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow("image")


cv2.createTrackbar("B","image",0,255,fxn)
cv2.createTrackbar("G","image",0,255,fxn)
cv2.createTrackbar("R","image",0,255,fxn)

switch="0: off\n 1:on"
cv2.createTrackbar("switch","image",0,1,fxn)

while(1):
    cv2.imshow("image", img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
    else:
        b=cv2.getTrackbarPos("B", "image")
        g = cv2.getTrackbarPos("G" ,"image")
        r = cv2.getTrackbarPos("R" ,"image")

        s=cv2.getTrackbarPos("switch", "image")

        if s==1:
            img[:]=[b,g,r]
        else:
            img[:]=0

cv2.destroyAllWindows()