import cv2


class Camera:
    def __init__(self, camera_id=0, width=640, height=480): #id 0 cuz inbuilt. change for pi later
        self.cap = cv2.VideoCapture(camera_id)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def capture(self):
        success, frame = self.cap.read()
        if not success:
            raise RuntimeError('Failed to capture image')
        return frame
    def release(self):
        self.cap.release()