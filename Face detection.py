import cv2
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml.txt")
img = cv2.imread("photo_2022-06-23 17.27.49.jpeg") 
#this stuff only reads image in gray color so we have to convert the image to gray
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face= face_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y), (x+w, y+h), (225,0,0), 2)

cv2.imshow('img', img)
cv2.waitKey()
cv2.imwrite("face detected", img)
