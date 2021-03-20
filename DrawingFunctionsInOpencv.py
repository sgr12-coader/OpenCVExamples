import cv2
img=cv2.imread("abc.png")
img=cv2.line(img,(0,0),(180,180),(234,33,43),5)

img=cv2.arrowedLine(img,(0,0),(60,80),(21,33,43),5)

img=cv2.rectangle(img,(300,0),(100,100), (232,31,123), 5)

img=cv2.circle(img, (100,100) ,100,(232,123,221), 2)

font=cv2.FONT_ITALIC
img=cv2.putText(img,"sgr",(10,132),font,4,(212,34,211),2,cv2.LINE_4)


cv2.imshow("image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

