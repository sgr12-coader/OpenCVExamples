import cv2

from matplotlib import pyplot as plt

img=cv2.imread("download.png", cv2.IMREAD_GRAYSCALE)
_,mask=cv2.threshold(img,80,255,cv2.THRESH_BINARY_INV)

import numpy as np
kernel=np.ones((5,5),np.uint8)

dilation=cv2.dilate(mask,kernel,iterations=2)

erosion=cv2.erode(mask,kernel,iterations=3 )

opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) #erosion followed by dilation
closeing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel) #first dilation then erosin
gradient=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)#diference between dilation and erosin
Tophat=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)#diference between image and opening
Rect=cv2.morphologyEx(mask,cv2.MORPH_RECT,kernel)
blackhat=cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel)
cross=cv2.morphologyEx(mask,cv2.MORPH_CROSS,kernel)
ellipse=cv2.morphologyEx(mask,cv2.MORPH_ELLIPSE,kernel)
erode=cv2.morphologyEx(mask,cv2.MORPH_ERODE,kernel)

titles=["Images","mask","dilation","erosion","opening","closeing","gradient","Tophat","Rect","blackhat","cross","ellipse","erode"]
images=[img,mask,dilation,erosion,opening,closeing,gradient,Tophat,Rect,blackhat,cross,ellipse,erode]

for i in range(13):
    plt.subplot(3,5 ,i+1), plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
