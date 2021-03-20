import cv2
img=cv2.imread("abc.png")
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(imggray,127,255,0)
countours,heirarchy=cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print("Numbers of countours is:  " ,str(len(countours)))

cv2.drawContours(img,countours,-1,(0,255,0),3) #-1 is for connecting all the countours we can also give indexing there

cv2.imshow("image",img)
cv2.imshow("inage2",imggray)
cv2.waitKey(0)
cv2.destroyAllWindows()