import cv2

#อ่านภาพ
img = cv2.imread("image/peoples.jpg")
#อ่านไฟล์สำหรับ classification
face_cascade=cv2.CascadeClassifier("Detect/haarcascade_frontalface_alt2.xml")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
count = 0
#จำแนกใบหน้า
scaleFactor = 1.1
minNeighber = 4
face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)

#แสดงตำแหน่งที่เจอใบหน้า
for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=5)
    count += 1


cv2.putText(img,"peoples value is "+str(count), (10,30), cv2.FONT_HERSHEY_SIMPLEX,  1, (255, 0, 255), 2)
#แสดงภาพ
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()