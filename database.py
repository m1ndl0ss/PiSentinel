import os
import faceRecognition
import face_recognition

def get_known_faces():
    known_faces = {}
    for filename in os.listdir('known_faces'):
        if filename.endswith(('.jpg', '.png')):
            path = os.path.join('known_faces', filename)
            image = faceRecognition.load_image_file(path)
