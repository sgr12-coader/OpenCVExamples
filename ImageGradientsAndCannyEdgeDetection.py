import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("dhoni.jpg",cv2.IMREAD_GRAYSCALE)
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

lap=cv2.Laplacian(img, cv2.CV_64F,ksize=3 )
lap=np.uint8(np.absolute(lap))

SobalX=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
SobalX=np.uint8(np.absolute(SobalX))

SobalY=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
SobalY=np.uint8(np.absolute(SobalY))

SobalCombine=cv2.bitwise_or(SobalX,SobalY)


canny=cv2.Canny(img,100,200)


titels=["Image","Laplacian","SobalX","SobalY","Combine Sobal","canny"]
images=[img,lap,SobalX,SobalY,SobalCombine,canny]

for i in range(6):
    plt.subplot(3,2,i+1),plt.imshow(images[i],"gray")
    plt.title(titels[i])
    plt.xticks([]),plt.yticks([])

plt.show()
