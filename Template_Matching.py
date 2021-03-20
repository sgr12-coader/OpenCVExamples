import cv2
import numpy as np
dhoni=cv2.imread("dhoni.jpg")
img=cv2.imread("dhoni.jpg",0)
ball=cv2.imread("ball.jpg",0)

w,h=ball.shape[::-1]

#result=cv2.matchTemplate(img,ball,cv2.TM_CCOEFF_NORMED)
result1=cv2.matchTemplate(img,ball,cv2.TM_CCORR_NORMED)
print(result1)
#we have to find largest value in printed array
threshold=0.95
loc=np.where(result1>=threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(dhoni,pt,(pt[0] +w, pt[1] +h),(0,255,0),1)

cv2.imshow("IMage",dhoni)
cv2.waitKey(0)
cv2.destroyAllWindows()