import cv2
import requests
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
import paho.mqtt.client as mqtt
host = "broker.hivemq.com"
port = 1883
client = mqtt.Client()
client.connect(host)

fan_status = "OFF"
pum_status = "OFF"

def on_message(client, userdata, msg):
    global fan_status, pum_status
    payload_str = msg.payload.decode('utf-8') 
    print(f"{msg.topic} {payload_str}")
    if msg.topic == 'fan1' and str(msg.payload.decode('utf-8')) == '1':
        fan_status = 'ON'
    elif msg.topic == 'fan2':
        fan_status = 'OFF'
    elif msg.topic == 'pum1' and str(msg.payload.decode('utf-8')) == '1':
        pum_status = 'ON'
    elif msg.topic == 'pum2':
        pum_status = 'OFF'

client.on_message = on_message
client.subscribe('fan1')
client.subscribe('fan2')
client.subscribe('pum1')
client.subscribe('pum2')

client.loop_start()

line_notify_token = 'gq1UEDWLSHiKyi6se413IQGjqnK1ATn3O6ZLzmtccf3'

def linenotify(message):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    data = {'message': message}
    session = requests.Session()
    session.post(url, headers=headers, data=data)


# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Initially set finger count to 0 for each cap
    fingerCount = 0

    if results.multi_hand_landmarks:

      for hand_landmarks in results.multi_hand_landmarks:
        # Get hand index to check label (left or right)
        handIndex = results.multi_hand_landmarks.index(hand_landmarks)
        handLabel = results.multi_handedness[handIndex].classification[0].label

        # Set variable to keep landmarks positions (x and y)
        handLandmarks = []

        # Fill list with x and y positions of each landmark
        for landmarks in hand_landmarks.landmark:
          handLandmarks.append([landmarks.x, landmarks.y])

        # Test conditions for each finger: Count is increased if finger is 
        #   considered raised.
        # Thumb: TIP x position must be greater or lower than IP x position, 
        #   deppeding on hand label.
        if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
          fingerCount = fingerCount+1
        elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
          fingerCount = fingerCount+1

        # Other fingers: TIP y position must be lower than PIP y position, 
        #   as image origin is in the upper left corner.
        if handLandmarks[8][1] < handLandmarks[6][1]:       #Index finger
          fingerCount = fingerCount+1
        if handLandmarks[12][1] < handLandmarks[10][1]:     #Middle finger
          fingerCount = fingerCount+1
        if handLandmarks[16][1] < handLandmarks[14][1]:     #Ring finger
          fingerCount = fingerCount+1
        if handLandmarks[20][1] < handLandmarks[18][1]:     #Pinky
          fingerCount = fingerCount+1

        # Draw hand landmarks 
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    
    if fingerCount == 5:
      client.publish("pum1","1")
    elif fingerCount == 10:
      client.publish("pum2","0")
    elif fingerCount == 3 :
      message = 'คุณชูสามนิ้ว'  
      linenotify(message)
    elif fingerCount == 2:
      client.publish("fan1","1")
    elif fingerCount == 4:
      client.publish("fan2","0")
      
      
    # Display finger count
    cv2.putText(image, str(fingerCount), (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 0), 10)
    cv2.putText(image, f"pum: {pum_status}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.putText(image, f"fan: {fan_status}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    

    # Display image
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()