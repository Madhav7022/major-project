import pytesseract
import cv2
from PIL import Image
import os
import pyttsx3


# camera.py
import camera
camera.print_class_name()  # Call a function from camera.py

# file1.py
import subprocess
subprocess.run(["python", "camera.py"])

language = 'en+ka'
engine = pyttsx3.init()
engine.setProperty('rate', 100) 
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
    try:
        check, frame = webcam.read()
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('z'):
            cv2.imwrite(filename='save_img.jpg', img=frame)
            webcam.release()
            string = pytesseract.image_to_string('save_img.jpg')
            print(string)
            engine.setProperty('rate', 125) 
            #engine.say("hi")
            engine.say(string)
            engine.runAndWait()
            print("Image saved!")
            cv2.destroyAllWindows()
            break
            
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break