import cv2
import numpy as np
import struct
from matplotlib import pyplot as plt 
import serial
ser=serial.Serial('COM3',9600)
#p=ser.readline()
#print(p)
'''def servo(x):
    ser=serial.Serial('COM3',9600)
    ser.write(repr(x).encode())'''
    
#import pyautogui
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    roi=frame[50:250,50:250]
    cv2.rectangle(frame,(50,50),(250,250),(0,255,0),2)
    cv2.line(frame,(150,50),(150,250),(0,0,0),4)
    blur=cv2.GaussianBlur(roi,(3,3),0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    lb=np.array([155,120,100])
    ub=np.array([179,255,255])
    mask=cv2.inRange(hsv,lb,ub)
    kernel=np.ones((5,5))
    dilate=cv2.dilate(mask,kernel,iterations=3)
    erosion=cv2.erode(dilate,kernel,iterations=3)
    filteration=cv2.GaussianBlur(dilate,(3,3),0)
    ret,thresh=cv2.threshold(filteration,127,255,cv2.THRESH_BINARY)
    contours,hierarchy= cv2.findContours(filteration,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(roi,contours,-1,(0,0,250),3)
    for c in contours:
        area=sorted(c, key = cv2.contourArea, reverse = True)[0]
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        cv2.circle(roi, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        M=cv2.moments(c)
        cx=int(M["m10"] / M["m00"])
        cy=int(M["m01"] / M["m00"])
        #servo(cx)
        print(cx)
        cv2.circle(roi, (cx, cy), 5, (255, 255, 255), -1)
        if cx>100 and cx<200:
            cv2.putText(frame,'right',(500,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),cv2.LINE_AA) 
            
            ser.write(struct.pack('>B', cx))                                                                                            
        elif cx<100 and cx>0:
            cv2.putText(frame,'left',(500,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),cv2.LINE_AA)
            #val='0'
            ser.write(struct.pack('>B', cx))   
    cv2.imshow('frame',frame)
    cv2.imshow('roi',roi)
    cv2.imshow('mask',mask)
    k=cv2.waitKey(1)
    if k==27:
        break


cap.release()
cv2.destroyAllWindows()


    