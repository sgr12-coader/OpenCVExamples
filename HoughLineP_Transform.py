import cv2
import numpy as np
img=cv2.imread("sudoko.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
CannyEdges=cv2.Canny(gray, 50,100,apertureSize=3)
cv2.imshow("canny",CannyEdges)
lines=cv2.HoughLinesP(CannyEdges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for li in lines:
    x1,y1,x2,y2=li[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),5)


cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
