import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#
# address = "https://172.16.15.203:8080/video"
# cap.open(address)
#
back = cv2.imread('./image.jpg')

while cap.isOpened():
    #take each frame
    ret, frame = cap.read()

    if ret:
        #how to convt rgb to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv",hsv)
        #how to get the hsv value?
        #lower: hue -10,100,100, heigher: h+10, 255, 255
        red = np.uint8([[[0,0,0]]])#bgr value of red
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        #print hsv value of red from bgr 
        #print(hsv_red)
        

        #threshold the hsv value to get only red colors
        l_red = np.array([0,0,0])
        u_red = np.array([180,255, 30])
        
        mask = cv2.inRange(hsv, l_red,u_red)
        #cv2.imshow("mask",mask)

        #all things red
        part1 = cv2.bitwise_and(back, back, mask=mask)
        #cv2.imshow("part1",part1)

        mask = cv2.bitwise_not(mask)
        
        #part2 all thing not red
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        #cv2.imshow("mask",part2)
        part3 = part1 + part2
        cv2.imshow("clock", part3)    ####this will return in flutter project to mobile camera 

        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()