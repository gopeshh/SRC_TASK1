import numpy as np
import cv2
cap= cv2.VideoCapture(0)
while(1):
    ret,frame=cap.read()
    hsv= cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)
    lower_limit= np.array([0,0,255])
    upper_limit= np.array([180,255,255])
    mask = cv2.inRange(hsv,lower_limit,upper_limit)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

