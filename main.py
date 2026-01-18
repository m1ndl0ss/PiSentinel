from camera import Camera
from motion import motion_detected
from face_recognition import recognize_face
from database import load_known_faces

def main():
    camera = Camera()
    known_faces = load_known_faces("data/known_faces")
    try:
        while True:
            frame = camera.capture()
            if motion_detected(frame):
                name = recognize_face(frame)
                print(name) #for debug
    finally:
        camera.release()

if __name__ == "__main__":
    main()