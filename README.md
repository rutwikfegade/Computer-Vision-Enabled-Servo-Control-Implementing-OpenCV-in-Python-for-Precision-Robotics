# Computer Vision-Enabled Servo Control: Implementing OpenCV in Python for Precision Robotics
The object is located using its colour, after which a contour is drawn around it. The moment is then calculated and used to determine the object's centre. We can locate the object inside the box with the help of this centre. Now, the Arduino receives information about the object's movement via a serial port, and the servo is moved accordingly. As seen in the video, the middle line divides the box into the left and the right.
This project aims to control motors or any other type of device using computer vision.

## Project Components:

Color Recognition: The project initiates by identifying the object based on its color. This fundamental computer vision technique serves as the foundation for subsequent tracking and analysis.

Contour Drawing: After identifying the object, a contour is drawn around it. This step not only visually represents the recognized object but also lays the groundwork for calculating essential parameters.

Moment Calculation: The moments of the object's contour are computed to determine its center. This calculation provides crucial spatial information that becomes pivotal for further analysis and tracking.

Arduino-Servo Integration: Information about the object's movement is transmitted to an Arduino via a serial port. The Arduino processes this information and controls a servo motor accordingly, aligning it with the object's detected position.




https://user-images.githubusercontent.com/69248756/172686720-ba435306-8101-4e3c-a7f7-e29733764f54.mp4



