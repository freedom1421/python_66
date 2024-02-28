import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    # Check if landmarks are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the landmarks of the index finger and thumb
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # Convert landmarks to pixel coordinates
            h, w, _ = frame.shape
            index_finger_x, index_finger_y = int(index_finger.x * w), int(index_finger.y * h)
            thumb_x, thumb_y = int(thumb.x * w), int(thumb.y * h)

            # Calculate the distance between index finger and thumb
            distance = math.sqrt((index_finger_x - thumb_x)**2 + (index_finger_y - thumb_y)**2)

            # Display the distance on the frame
            cv2.putText(frame, f'Distance: {distance:.2f} pixels', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Draw circles at the index finger and thumb positions
            cv2.circle(frame, (index_finger_x, index_finger_y), 5, (255, 0, 0), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 5, (255, 0, 0), -1)

    # Display the frame
    cv2.imshow('Hand Landmarks', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
