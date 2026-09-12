import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

hands = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            draw.draw_landmarks(frame, hand,
                                mp.solutions.hands.HAND_CONNECTIONS)

            fingers = 0
            points = hand.landmark

            if points[8].y < points[6].y:
                fingers += 1
            if points[12].y < points[10].y:
                fingers += 1
            if points[16].y < points[14].y:
                fingers += 1

            if fingers == 1:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            elif fingers == 2:
                frame = cv2.GaussianBlur(frame, (15, 15), 0)

            elif fingers == 3:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.Canny(gray, 100, 200)

    cv2.imshow("Gesture Camera", frame)

    key = cv2.waitKey(1)

    if key == ord("p"):
        cv2.waitKey(0)  

    if key == ord("s"):
        cv2.imwrite("Photo.png", frame)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()