import cv2
import numpy as np
img1=cv2.imread("download.png")
img2=cv2.imread("abc.png")
print(img1.shape)
print(img2.shape)

#img1_2=np.hstack((img1[:,113], img2[:,113:]))

#Generate Gaussien pyramid for img1
img1_copy=img1.copy()
gp_img1=[img1_copy]
for i in range(6):
    img1_copy=cv2.pyrDown(img1_copy)
    gp_img1.append(img1_copy)

#Generate Gaussien pyramid for img2
img2_copy=img2.copy()
gp_img2=[img2_copy]
for i in range(6):
    img2_copy=cv2.pyrDown(img2_copy)
    gp_img2.append(img2_copy)

#Generate laplission pyramid for img1
img1_copy=gp_img1[5]
lp_img1=[img1_copy]
for i in range(5, 0, -1):
    gau_extented=cv2.pyrUp(gp_img1[i])
    laplission=cv2.subtract(gp_img1[i-1], gau_extented)
    lp_img1.append(laplission)

#Generate laplission pyramid for img2
img2_copy=gp_img2[5]
lp_img2=[img2_copy]
for i in range(5, 0, -1):
    gau_extented=cv2.pyrUp(gp_img2[i])
    laplission=cv2.subtract(gp_img2[i-1], gau_extented)
    lp_img2.append(laplission)

#for adding half half of both images
img1_img2_pyramid=[]
n=0
for img1_lap, img2_lap in zip(lp_img1,lp_img2):
    n +=1
    cols, rows,ch=img1_lap.shape
    laplission=np.hstack((img1_lap[:, 0:int(cols/2)],img2_lap[:, 0:int(cols/2)]))
    img1_img2_pyramid=img1_img2_pyramid.append(laplission)

#Now reconstruct
img1_img2_reconstruct=img1_img2_pyramid[0]
for i in range(1,6):
    img1_img2_reconstruct=cv2.pyrUp(img1_img2_reconstruct)
    img1_img2_reconstruct=cv2.add(img1_img2_pyramid[i],img1_img2_reconstruct)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img1_img2_reconstruct", img1_img2_reconstruct)


cv2.waitKey(0)
cv2.destroyAllWindows()