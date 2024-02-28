import cv2
import numpy

# แสดงคำว่า Open Camera
# เปิดการทำงานกล้อง
print("Open Camera")
cap = cv2.VideoCapture(0)

# ลูป วนการทำงาน
while True:
    # แสดงคำว่า stat loop
    print("stat loop")

    # จับภาพจากกล้อง
    ret, img = cap.read()

    # แสดงหน้าจอในชื่อ camera
    cv2.imshow('camera', img)

    # สั่งหยุดต่อเมื่อ กดตัว S
    k = cv2.waitKey(0)
    if k == ord('s'):
        break

# ปิดกล้อง
cap.release()

# ปิดหน้าต่าง
cv2.destroyAllWindows()
