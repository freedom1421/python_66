import cv2
import datetime
import time
import requests

cap = cv2.VideoCapture(0)
frameRate = cap.get(5)  
cur_time = time.time()
start_time_24h = cur_time
start_time_1min = cur_time - 59

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

line_notify_token = 'gq1UEDWLSHiKyi6se413IQGjqnK1ATn3O6ZLzmtccf3'

def linenotify(message, image_path=None):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + line_notify_token}

    data = {'message': message}
    session = requests.Session()
    session.post(url, headers=headers, data=data)

    if image_path:
        img = {'imageFile': open(image_path, 'rb')}
        session.post(url, headers=headers, files=img, data=data)

while cap.isOpened():
    check, frame = cap.read()

    if check:
        currentDate = str(datetime.datetime.now())
        cv2.putText(frame, currentDate, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), cv2.LINE_4)
        cv2.imshow("Output", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("s"):
            cv2.imwrite("output.jpg", frame)
            print("0xFF=")
            print(0xFF)

            message = 'Oh!'  
            linenotify(message, 'output.jpg')

        elif key == ord("p"):
            break  

        elif key == ord("v"):
            print("start rescord !!!")
            recording_start_time = time.time()
            recording_duration = 5  
            while time.time() - recording_start_time < recording_duration:
                ret, frame = cap.read()
                out.write(frame)
                currentDate = str(datetime.datetime.now())
                cv2.putText(frame, currentDate, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), cv2.LINE_4)
                cv2.imshow("Output", frame)
                cv2.waitKey(1)
            print("stop rescord !!!")

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
