import cv2
import mp_hands = mp.solutions.hands

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

filters = ["Normal", "Grayscale", "Sepia", "Negative", "Blur"]
filter_idx = 0
last_gesture_ms = 0
photo_counter = 0

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    current_ms = cv2.getTickCount() / (cv2.getTickFrequency() / 1000.0)

    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    if results.multi_hand_landmarks:
        lm = results.multi_hand_landmarks[0].landmark
        
        thumb = lm[mp_hands.HandLandmark.THUMB_TIP]
        index = lm[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        mid = lm[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        ring = lm[mp_hands.HandLandmark.RING_FINGER_TIP]
        pinky = lm[mp_hands.HandLandmark.PINKY_FINGER_TIP]

        dist = lambda p1, p2: np.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2 + (p1.z-p2.z)**2)

        if (current_ms - last_gesture_ms) > 1000.0:
            if dist(thumb, index) < 0.05:
                photo_counter += 1
                last_gesture_ms = current_ms
                
                cap_frame = frame.copy()
                if filters[filter_idx] == "Grayscale": cap_frame = cv2.cvtColor(cv2.cvtColor(cap_frame, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
                elif filters[filter_idx] == "Sepia": cap_frame = np.clip(cv2.transform(cap_frame, np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])), 0, 255).astype(np.uint8)
                elif filters[filter_idx] == "Negative": cap_frame = cv2.bitwise_not(cap_frame)
                elif filters[filter_idx] == "Blur": cap_frame = cv2.GaussianBlur(cap_frame, (21, 21), 0)
                
                cv2.imwrite(f"photo_{photo_counter}.png", cap_frame)

            elif dist(thumb, mid) < 0.05 or dist(thumb, ring) < 0.05 or dist(thumb, pinky) < 0.05:
                filter_idx = (filter_idx + 1) % len(filters)
                last_gesture_ms = current_ms

    if filters[filter_idx] == "Grayscale": frame = cv2.cvtColor(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
    elif filters[filter_idx] == "Sepia": frame = np.clip(cv2.transform(frame, np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])), 0, 255).astype(np.uint8)
    elif filters[filter_idx] == "Negative": frame = cv2.bitwise_not(frame)
    elif filters[filter_idx] == "Blur": frame = cv2.GaussianBlur(frame, (21, 21), 0)

    cv2.putText(frame, f"Filter: {filters[filter_idx]}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.imshow("App", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()

