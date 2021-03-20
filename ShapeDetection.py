import cv2
import numpy as np
img=cv2.imread("shapes.png",0)
#img=cv2.resize(img,(256,256))

_,thresh=cv2.threshold(img, 240,255 ,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for countour in contours:
    approx=cv2.approxPolyDP( countour, 0.01*cv2.arcLength(countour,True),True) #here0.01 is epsilon fiche defind accuracy
    # arcLength() calculate the contour parameter
    cv2.drawContours(img,[approx],0,(0,0,0),1)
    x=approx.ravel()[0]
    y=approx.ravel()[1]-5
    if len(approx)==3:
        cv2.putText(img,"Tringle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(44,225,0))
    elif len(approx)==4:
        cv2.putText(img,"rectangal",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(44,225,0))
    else:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (44, 225, 0))

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
