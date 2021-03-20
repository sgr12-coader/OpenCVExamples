import cv2
cap= cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc("X","V","I","D")
out= cv2.VideoWriter("output.mp4", fourcc, 20,  (640,480))
while(cap.isOpened()):
    ret, frame =cap.read()
    #gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

