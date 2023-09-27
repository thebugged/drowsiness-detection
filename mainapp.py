import cv2
import numpy as np
from keras.models import model_from_json
from tensorflow.keras.preprocessing.image import img_to_array

# Loading the model
json_file = open('drowsy.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
classifier = model_from_json(loaded_model_json)
classifier.load_weights("drowsy.h5")

# Initialize the face cascade classifier
face_cascade = cv2.CascadeClassifier('./test/haarcascade_frontalface_default.xml')

# Define a dictionary to map model output classes
emotion_dict = {0: 'Alert', 1: 'Drowsy', 2:'Alert', 3: 'Drowsy'}

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

   # Inside the loop for processing each frame
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        
        # Resize the grayscale face region to 145x145 pixels
        roi_gray_resized = cv2.resize(roi_gray, (145, 145))
        
        # Convert the resized grayscale image to RGB format
        roi_rgb = cv2.cvtColor(roi_gray_resized, cv2.COLOR_GRAY2RGB)  # Convert to RGB

        if np.sum([roi_gray]) != 0:
            roi = roi_rgb.astype('float') / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            # Make predictions using your drowsiness detection model
            prediction = classifier.predict(roi)[0]
            maxindex = int(np.argmax(prediction))
            final_out = emotion_dict[maxindex]

            label_position = (x, y)
            cv2.putText(frame, final_out, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame with annotations
    cv2.imshow('Drowsiness Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
