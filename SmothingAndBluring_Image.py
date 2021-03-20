import cv2
from matplotlib import pyplot as plt
import numpy as np

img=cv2.imread("abc.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel= np.ones((5,5), np.float32)/25
dst=cv2.filter2D(img,-1,kernel)

blr=cv2.blur(img,(5,5))

gblr=cv2.GaussianBlur(img,(5,5),0)#designed for removine high frequency noise

median=cv2.medianBlur(img,5) #For removing Salt and paper dots

bilateral=cv2.bilateralFilter(img,9,75,75)#edge sharping

titles=["IMage","filter2D","blur","GaussianBlur","medianBlu","bilateralFilter"]
images=[img,dst,blr,gblr,median,bilateral]

for i in range(6):
    plt.subplot(2, 3 ,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.yticks([]),plt.xticks([])

plt.show()