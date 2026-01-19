import cv2
import face_recognition
import numpy as np


def recognise_face(frame, known_faces, tolerance=0.7):
    # Convert BGR to RGB and force a copy
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).copy()

    # Force it to be exactly what face_recognition wants
    rgb_frame = np.ascontiguousarray(rgb_frame, dtype=np.uint8)

    location = face_recognition.face_locations(rgb_frame)
    encodings = face_recognition.face_encodings(rgb_frame, location)
    for face_encoding in encodings:
        for name, known_encoding in known_faces.items():
            match = face_recognition.compare_faces([known_encoding], face_encoding, tolerance=tolerance)
            if match[0]:
                return name
    return None