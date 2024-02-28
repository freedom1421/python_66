import cv2
#อ่านภาพ
img = cv2.imread("image/cat.jpg")
#กำหนดขนาด
imgresize = cv2.resize(img,(700,700))
#วาดสี่เหลี่ยม
# rectangle(ภาพ,มุมที่ 1 (บนซ้าย),มุมที่ 2 (ล่างขวา),สี,ความหนา)
cv2.rectangle(imgresize,(100,100),(500,500),(0,255,255),10)
cv2.rectangle(imgresize,(200,200),(600,600),(255,0,255),10)
cv2.rectangle(imgresize,(30,550),(250,250),(0,0,255),10)
cv2.rectangle(imgresize,(10,30),(400,300),(0,255,0),10)
cv2.putText(imgresize, "4554242", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 100, (0,255,255))
cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()