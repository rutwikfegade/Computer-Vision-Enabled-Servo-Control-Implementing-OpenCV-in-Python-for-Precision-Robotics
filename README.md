## using-opencv-to-control-a-servo
The colour of the object is used to detect it, and then a contour is made around it.
After that, we calculate the moment and use it to find the object's centre.
This centre assists us in determining the location of the object within the box.
Now, the data of the object's movement is communicated to the Arduino via serial port, and the servo is moved accordingly.
The middle line divides the box into left and right as shown in the video.






https://user-images.githubusercontent.com/69248756/172686720-ba435306-8101-4e3c-a7f7-e29733764f54.mp4



