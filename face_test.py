import cv2
import os

# แสดงคำว่า Open Camera
# เปิดการทำงานกล้อง
print("Open Camera")
cam = cv2.VideoCapture(0)

# ฟังชัน เงื่อนไข การสร้างและจับเก็บ folder
def assure_path_exists(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

# ฟังชัน ตรวจจับใบหน้า
def detect_face(image_frame):
    # แสดงคำว่า capture
    print("capture")

    # แสดงเฟรมที่จับเป็นสีเทา
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # ตรวจจับใบหน้าเฉพาะในกรอบที่กำหนด
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # loop for
    for (x, y, w, h) in faces:
        # ตัดรูปในกรอบที่ตรวจจับ
        cv2.rectangle(image_frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # จัดเก็บภาพใน folder ที่กำหนด
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".png", gray[y:y+h, x:x+w])

    # แสดงหน้าจอกล้อง
    cv2.imshow('dataset', image_frame)

# ตรวจจับวัตถุ โดยใช้ ฟังชัน cv2.CascadeClassifier
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# กำหนด id ต่อคน
print("Input id:")
face_id = input()

# เริ่มนับจาก 0
count = 0

# นำไปวางใน folder ที่กำหนด
assure_path_exists("dataset/")

# ลูบ วนการทำงาน
while True:
    # แสดงคำว่า start loop
    print("start loop")

    # จับภาพเป็นเฟรม
    ret, image_frame = cam.read()

    # detect face
    detect_face(image_frame)

    # สั่งหยุดต่อเมื่อ กด 's'
    if cv2.waitKey(50) & 0xFF == ord('s'):
        break

    # count += 1
    count += 1

    # ถ้าภาพเกิน 50 ให้หยุดทำงาน
    if count > 50:
        break

# ปิดกล้อง
cam.release()

# ปิดหน้าต่าง
cv2.destroyAllWindows()
