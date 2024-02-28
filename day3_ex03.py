import cv2
#อ่านภาพ
img = cv2.imread("image/cat.jpg")
#กำหนดขนาด
imgresize = cv2.resize(img,(700,700))
#วาดวงกลม
# circle(ภาพ,ตำแหน่งจุดศูนย์กลางวงกลม (x,y),รัศมี,สี,ความหนา)
cv2.circle(imgresize,(350,470),150,(0,0,255),5)
cv2.circle(imgresize,(420,280),150,(255,0,0),5)
cv2.circle(imgresize,(280,280),150,(0,255,0),5)
cv2.circle(imgresize,(350,350),300,(0,255,255),5)
cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()