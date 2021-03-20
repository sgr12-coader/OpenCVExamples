import cv2
import datetime
cap=cv2.VideoCapture(0)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(height,width)
cap.set(3,  1280)
cap.set(4, 720)
datet=str(datetime.datetime.now())


while(cap.isOpened()):
    ret, frame=cap.read()
    if ret ==True:
        font=cv2.FONT_HERSHEY_TRIPLEX
        text="width:- "+str(cap.get(3)) + " height:- "+str(cap.get(4))
        frame=cv2.putText(frame,text,(10,100),font,1,(234,123,432),2,cv2.LINE_8)
        frame = cv2.putText(frame, datet, (200, 100), font, 1, (0, 123, 43), 2, cv2.LINE_8)
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF ==ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()