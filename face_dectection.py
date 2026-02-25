import cv2
import cv2.data
import os

#print(os.listdir(cv2.data.haarcascades))
traning_file = "haarcascade_frontalface_default.xml"
file_path = cv2.data.haarcascades + traning_file


#print("Model traning")

img = cv2.imread("secondImage.jpg")


faces = modal.detectMultiScale(img,1.2,4)

for face in faces:
    x1 = face[0]
    y1 = face[1]
    x2 = x1 + face[2]
    y2 = y1 + face[3]
    cv2.rectangle(img,(x1,y1),(x2,y2),[208,253,255],2)

#color = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)               #color ke liye

new_img = cv2.resize(img,(500,700))
cv2.imshow("this is my image",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()