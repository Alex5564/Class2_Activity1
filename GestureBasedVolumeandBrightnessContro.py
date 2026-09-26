import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
        
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            
            thumb_x = int(landmarks[4].x * w)
            thumb_y = int(landmarks[4].y * h)
            index_x = int(landmarks[8].x * w)
            index_y = int(landmarks[8].y * h)

            cv2.circle(frame, (thumb_x, thumb_y), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(frame, (index_x, index_y), 10, (255, 0, 0), cv2.FILLED)

            dx = index_x - thumb_x
            dy = index_y - thumb_y
            distance = (dx*dx + dy*dy) ** 0.5

            level = (distance - 20) / (200 - 20) * 100
            if level < 0: level = 0
            if level > 100: level = 100

            cv2.putText(frame, f"Value: {int(level)}%", (thumb_x, thumb_y - 20), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Simple Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
