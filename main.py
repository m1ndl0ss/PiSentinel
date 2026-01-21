
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

# from camera import Camera
# from motion import Motion
# from faceRecognition import recognise_face
# from database import load_known_faces
# import numpy as np
# import cv2
#
#
# def main():
#     camera = Camera()
#     frame = camera.capture()
#
#     print(f"Frame shape: {frame.shape}")
#     print(f"Frame dtype: {frame.dtype}")
#     print(f"Frame min/max: {frame.min()}/{frame.max()}")
#     print(f"Frame is uint8: {frame.dtype == np.uint8}")
#
#     # Try converting
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     print(f"RGB shape: {frame_rgb.shape}")
#     print(f"RGB dtype: {frame_rgb.dtype}")
#
#     camera.release()
#
# if __name__ == "__main__":
#     main()
