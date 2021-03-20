import cv2
img=cv2.imread("abc.png")
leyer=img.copy()
GP=[leyer]

for i in range(5):
    leyer=cv2.pyrDown(leyer)
    GP.append(leyer)
    # cv2.imshow(str(i),leyer)
leyer=GP[4]
cv2.imshow("Lavel UP gaussein Pyrmid",leyer)
LP=[leyer]

for i in range(4,0,-1):
    Gaussion_Extended= cv2.pyrUp(GP[i])
    Laplassion=cv2.subtract(GP[i-1], Gaussion_Extended)
    cv2.imshow(str(i), Laplassion)

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
