import cv2
img=cv2.imread("dhoni.jpg")

print(img.shape) #returns tumpels of numbers of roys cols and channels
print(img.size) #return total no of pixels is accessed
print(img.dtype) #return image datatype is obtained

# b, g,r=cv2.split(img)
# print("blue")
# print(b)
# print("Green")
# print(g)
# print("red")
# print(r)
# img=cv2.merge((b,g,r))

# ball=img[930:414 , 872:341]
# img[181:149, 162:176]= ball
img1=cv2.imread("abc.png")
img=cv2.resize(img,(512,512))
img1=cv2.resize(img1,(512,512))
#dst=cv2.add(img,img1)

dst=cv2.addWeighted(img,.9,img1,.9,0)

cv2.imshow("image",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
