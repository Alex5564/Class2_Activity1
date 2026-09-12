import cv2
import mediapipe as mp
import pyautogui
import math

hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)
frame_count = 0
last_scroll = 0

while cap.isOpened():
    success, frame = cap.read()
    if not success: continue

    frame_count += 1
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    gesture = None
    
    if results.multi_hand_landmarks:
        lm = results.multi_hand_landmarks[0].landmark

        ext = [lm[i].y < lm[i-2].y for i in]
        gesture = "up" if all(ext) else ("down" if not any(ext) else None)
        
        dist = math.sqrt((lm[4].x*w - lm[8].x*w)**2 + (lm[4].y*h - lm[8].y*h)**2)
        speed = max(5, int((dist / 100) * 20))

        if gesture and (frame_count - last_scroll > 10):
            pyautogui.scroll(speed if gesture == "up" else -speed)
            last_scroll = frame_count

    cv2.putText(frame, f"Action: {gesture}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow("Scroll", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()


