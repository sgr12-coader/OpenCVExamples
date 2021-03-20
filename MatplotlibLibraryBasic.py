import cv2
from matplotlib import pyplot as plt
img= cv2.imread("dhoni.jpg")
cv2.imshow("image",img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#Opencv reads an image in BGR formate while Matplotlib reads in a RBG formate
#so before reading image using matplotlib we need to convert image color from BGR to RBG

plt.imshow(img)
plt.xticks([]),plt.yticks([]) #removes x and y axics
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()