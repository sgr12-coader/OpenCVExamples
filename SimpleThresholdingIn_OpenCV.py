import cv2
img= cv2.imread("copy.jpg", 0)
_,th1=cv2.threshold(img,70,255, cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,70,255, cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,70,255, cv2.THRESH_TRUNC) #if pixel value if les or equl 70
# then it remain unchange# and if more than 70 it will be fixed to 70
_,th4=cv2.threshold(img,70,255, cv2.THRESH_TOZERO)#if pixel value if greater or equl 70
# then it remain unchange# and if less than 70 it will be fixed to 0
_,th5=cv2.threshold(img,70,255, cv2.THRESH_TOZERO_INV)
_,th6=cv2.threshold(img,70,255, cv2.THRESH_TRIANGLE)
_,th7=cv2.threshold(img,70,255, cv2.THRESH_MASK)
_,th8=cv2.threshold(img,70,255, cv2.THRESH_OTSU)


# cv2.imshow("Image",img)
# cv2.imshow("Threshold",th1)
# cv2.imshow("Threshold1_inv1",th2)
# cv2.imshow("Threshold2",th3)
# cv2.imshow("Threshold3",th4)
# cv2.imshow("Threshold4_inv3",th5)
# cv2.imshow("Threshold5",th6)
# cv2.imshow("Threshold6",th7)
# cv2.imshow("Threshold7",th8)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# Lets show the Images with Matplotlib

from matplotlib import pyplot as plt
titles= ["orignal","THRESH_BINARY","THRESH_BINARY_INV","THRESH_TRUNC",
         "THRESH_TOZERO","THRESH_TOZERO_INV","THRESH_TRIANGLE","THRESH_MASK","THRESH_OTSU"]
images=[img,th1,th2,th3,th4,th5,th6,th7,th8]

for i in range(9):
    plt.subplot(3,3,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])


plt.show()