import cv2
import numpy as np
from matplotlib import pylab as plt
img=cv2.imread("laneboth.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(img.shape)
height= img.shape[0]
width= img.shape[1]
region_of_intrest_vertices= [
    (0,height),
    (width/2,height/2),
    (width,height)
    ]

def region_of_intrest(img,vertices):
    mask= np.zeros_like(img)
    match_mask_color=255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image=cv2.bitwise_and(img,mask)
    return masked_image

def draw_lines(img,lines):
    img=np.copy(img)
    blank_image= np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint32)

    for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,0),thickness=5)

    img=cv2.addWeighted(img,0.8,blank_image,1,0.0)
    return img

gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
canny=cv2.Canny(gray,100,200)
cropped_img=region_of_intrest(canny,np.array([region_of_intrest_vertices], np.uint32))
lines=cv2.HoughLinesP(cropped_img,
                      rho=6,theta=np.pi/180,
                      threshold=160,
                      lines=np.array([]),
                      minLineLength=40,
                      maxLineGap=25)

img_with_lines= draw_lines(img,lines)
plt.imshow(img_with_lines)
plt.show()