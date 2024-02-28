import cv2
import requests
import os

cap = cv2.VideoCapture(0)
url = 'http://localhost:7001/face-register'

# Display the resulting frame
userid = input("Enter user id : ")
while(1):
  ret, frame = cap.read()
  cv2.imshow('Press S to save Picture',frame)
  key = cv2.waitKey(1)
  if key & 0xFF == ord('s'):
    image_path = 'input/'+userid+'.jpg'
    cv2.imwrite(image_path, frame)
    image_filename = os.path.basename(image_path)
    print("userid=" + userid)
    multipart_form_data = {
        'photo': (image_filename, open(image_path, 'rb')),
    }
 
    response = requests.post(url, data={'username': userid}, files=multipart_form_data)
    print(response.content)