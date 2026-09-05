import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

emotion_net = cv2.dnn.readNetFromONNX('emotion_model.onnx')

EMOTION_LABELS = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        roi_gray = gray_frame[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        
        blob = cv2.dnn.blobFromImage(
            roi_gray, 
            scalefactor=1.0 / 255.0, 
            size=(48, 48), 
            mean=(0,), 
            swapRB=False, 
            crop=False
        )
        
        emotion_net.setInput(blob)
        prediction = emotion_net.forward()
        
        max_index = np.argmax(prediction)
        predicted_emotion = EMOTION_LABELS[max_index]
        
        cv2.putText(
            frame, 
            predicted_emotion, 
            (x, y - 10), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1, 
            (0, 255, 0), 
            2
        )

    cv2.imshow('Real-time Emotion Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
