# Working

## Color Identification Process

The system begins by capturing images of the incoming balls using a camera connected to the Raspberry Pi. 
Image processing techniques, such as OpenCV-based color detection, are used to identify the color of each ball. 
The algorithm classifies the balls into predefined categories—**Pink**, **Yellow**, and **Orange**, etc.—based on their RGB or HSV values.
![image](https://github.com/user-attachments/assets/615bb76c-e4b4-4404-84d6-2eb5ec34dcb8)

## Servo Mechanism and Raspberry Pi Integration

The Raspberry Pi acts as the central processing unit, controlling the servo motors based on the detected color. 
When a ball is identified, the corresponding servo motor is triggered to guide the ball into its designated collection box. 
Two servo motors are used to handle the movement and sorting process efficiently.
![image](https://github.com/user-attachments/assets/06a6abaa-2af0-4150-871f-3b0b0ee348fd)

## Sorting Mechanism Based on Color Detection

- If a **Pink** ball is detected, the first servo motor moves to direct it into the pink collection box.  
- If a **Yellow** ball is detected, the first servo motor moves differently to allow it to reach the yellow box.  
- If an **Orange** ball is detected, the servo mechanism ensures it is directed to the orange collection box.
![image](https://github.com/user-attachments/assets/14fa460a-9ab5-4f71-b69f-2883856a5ca7)
