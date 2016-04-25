from module import Module

class MotionDetector(Module):

    callback = "Motion Detected"

    def __init__(self):
        super(MotionDetector, self).__init__(MotionDetector.callback)
