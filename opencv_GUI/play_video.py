import numpy as np 
import cv2 as cv 
cap=cv.VideoCapture('test.avi')#摄像机索引改成视频文件名
while True:
    ret,frame=cap.read()
    if not ret:
        print("Can't not receive frame(stream end?). Exiting...")
        break
    gray=cv.cvtColor(frame,cv.COLOR_BAYER_BG2BGR_EA)
    cv.imshow("frame",gray)
    if cv.waitKey(1)==ord('q'):
        break
cap.release()
cv.destroyAllWindows()