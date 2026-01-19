import cv2

class Motion:
    def __init__(self, pixelIntensityTreshold =30, blurSensitivity=21,pixelCountThreshold=25):
        self.previous_frame = None
        self.pixelIntensityThreshold = pixelIntensityTreshold
        self.blurSensitivity = blurSensitivity
        self.pixelCountThreshold=pixelCountThreshold

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #1 gray channel is sufficient
        gray = cv2.GaussianBlur(gray, (self.blurSensitivity,self.blurSensitivity), 0)

        if self.previous_frame is None:
            self.previous_frame = gray
            return False
        #find difference

        frame_diff = cv2.absdiff(self.previous_frame, gray)
        thresh = cv2.threshold(frame_diff, self.pixelIntensityThreshold, 255, cv2.THRESH_BINARY)[1] #converts the diff into black and white image where white- movement
        #self-note : threshbinary sets to max value if pixel exceeds thresh, otherwise to 0, we get black n white
        motion_pixels = cv2.countNonZero(thresh)

        return motion_pixels >self.pixelCountThreshold
