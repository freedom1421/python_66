import cv2
from deepface import DeepFace

# อ่านภาพ
img = cv2.imread("image/test.jpg")
img = cv2.resize(img,(800,600))
result = DeepFace.analyze(img, actions=['age', 'gender', 'emotion', 'race'], enforce_detection=False)
print(result)
count_man = 0
for x in result :
    print(x)
    if x['dominant_gender'] == 'Man':
        count_man += 1
    

