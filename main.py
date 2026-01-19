from camera import Camera
from motion import Motion
from faceRecognition import recognise_face
from database import load_known_faces

def main():
    camera = Camera()
    motion_detected = Motion()
    known_faces = load_known_faces("data/known_faces")
    try:
        while True:
            frame = camera.capture()
            if motion_detected.detect(frame):
                name = recognise_face(frame, known_faces)
                print(name) #for debug
    finally:
        camera.release()

if __name__ == "__main__":
    main()