import cv2 
import cv2.data


#print(os.listdir(cv2.data.haarcascades))
traning_file = "haarcascade_frontalface_default.xml"
file_path = cv2.data.haarcascades + traning_file


cam = cv2.VideoCapture(0)
modal = cv2.CascadeClassifier(file_path)

while True:
    status,image = cam.read()
    if status == False:
        print("camera is not supporting")
        break
    faces = modal.detectMultiScale(image,1.3,5)
    for face in faces:
        x1 = face[0]
        y1 = face[1]
        x2 = x1 + face[2]
        y2 = y1 + face[3]
        cv2.rectangle(image,(x1,y1),(x2,y2),[255,0,0],2)
    cv2.imshow ("Image",image)
    
    key = cv2.waitKey(1)
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
    
    