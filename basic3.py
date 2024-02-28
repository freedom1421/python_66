#อ่านภาพ
import cv2
img = cv2.imread("image/cat.jpg")
imgresize = cv2.resize(img,(400,400))
#แสดงภาพ
cv2.imshow("show",imgresize)
k =cv2.waitKey(0)
print ("key=>")
print (k)
if k == 27:
    cv2.destroyAllWindows()