import os
import face_recognition

def load_known_faces(directory):
    known_faces = {}
    for filename in os.listdir(directory):
        if filename.endswith(('.jpg', '.png')):
            path = os.path.join(directory, filename)
            image = face_recognition.load_image_file(path)
            encoding=face_recognition.face_encodings(image)

            if encoding:
                name = os.path.splitext(filename)[0]
                known_faces[name] = encoding[0]
            else:
                print(f"Warning : No face found in {filename}")
    return known_faces


