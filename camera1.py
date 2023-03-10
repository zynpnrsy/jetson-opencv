import cv2
import numpy as np

cam_jetson = cv2.VideoCapture(0)

while True:
        ret,goruntu = cam_jetson.read()
        cv2. imshow("gokcen",goruntu)

        if cv2.waitKey(30) & 0xFF == ("x"):
            break


cam_jetson.release()

cv2.destroyAllWindows

