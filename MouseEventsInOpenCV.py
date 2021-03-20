import cv2
img=cv2.imread("dhoni.jpg")

def click_fxn(event,x,y,flags, param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        font=cv2.FONT_HERSHEY_DUPLEX
        srtXY =str(x)+", "+str(y)
        cv2.putText(img, srtXY ,(x,y),font,1,(232,45,12),2)
        cv2.imshow("image",img)

    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv2.FONT_ITALIC
        strBGR=str(blue)+", "+str(green)+", "+str(red)
        cv2.putText(img, strBGR, (x, y), font, 1, (2, 235, 12), 1)
        cv2.imshow("image", img)


cv2.imshow("image",img)

cv2.setMouseCallback("image",click_fxn)

cv2.waitKey(0)
cv2.destroyAllWindows()