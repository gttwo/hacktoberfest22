import cv2


cap = cv2.VideoCapture(0) 
#
# address = "https://172.16.15.203:8080/video"###we will fetch ip address of mobile from flutter if it possible 
# cap.open(address)
#
while cap.isOpened():
    ret, back = cap.read() #reading from cam  ### read mobile cam using flutter
    if ret:
        cv2.imshow('IPWebcam', back)
        if cv2.waitKey(5) == ord('q'): ###on the place of q we will add flutter click button to capture image 
            # save the image
            cv2.imwrite('image.jpg', back)#### return clicked img to flutter project
            break

cap.release()
cv2.destroyAllWindows()