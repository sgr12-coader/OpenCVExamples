import cv2
import numpy as np
# from matplotlib import pyplot as plt
# for i in range(3):
#     plt.subplot(1,3,i+1),plt.imshow(images[i],"gray")
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

img=cv2.imread("abc.png")
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

lr1=cv2.pyrDown(img)#original resolution/2
lr2=cv2.pyrDown(lr1)#original resolution/4
lr3=cv2.pyrDown(lr2)#original resolution/8
ur1=cv2.pyrUp(img)#original resolution*2
# image quality decreases when we increase reso.
ur2=cv2.pyrUp(ur1)#original resolution*4
ur3=cv2.pyrUp(ur2)#original resolution*8

cv2.imshow("orignal image",img)

cv2.imshow("PyrDOWN image1",lr1)
cv2.imshow("PyrDOWN image2",lr2)
cv2.imshow("PyrDOWN image3",lr3)

cv2.imshow("PyrUP image1",ur1)
cv2.imshow("PyrUP image2",ur2)
cv2.imshow("PyrUP image3",ur3)

cv2.waitKey(0)
cv2.destroyAllWindows()



