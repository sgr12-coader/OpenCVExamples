import  cv2
import numpy as np

def fxn(x):
    pass

cv2.namedWindow("Tracking")

cv2.createTrackbar("LH", "Tracking",0,255,fxn)
cv2.createTrackbar("LS", "Tracking",0,255,fxn)
cv2.createTrackbar("LV", "Tracking",0,255,fxn)

cv2.createTrackbar("UH", "Tracking",255,255,fxn)
cv2.createTrackbar("US", "Tracking",255,255,fxn)
cv2.createTrackbar("UV", "Tracking",255,255,fxn)

while(True):
    frame=cv2.imread("dhoni.jpg")
    frame=cv2.resize(frame,(300,300))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lh =cv2.getTrackbarPos("LH", "Tracking")
    ls = cv2.getTrackbarPos("LS", "Tracking")
    lv = cv2.getTrackbarPos("LV", "Tracking")

    uh = cv2.getTrackbarPos("UH", "Tracking")
    us = cv2.getTrackbarPos("US", "Tracking")
    uv = cv2.getTrackbarPos("UV", "Tracking")

    L_B=np.array([lh, ls, lv])
    U_B=np.array([uh, us, uv])

    mask=cv2.inRange(hsv, L_B, U_B)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("Result",res)
    cv2.imshow("mask",mask)



    k =cv2.waitKey(1) &0xFF
    if k==27:
        break

cv2.destroyAllWindows()