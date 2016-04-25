from serial import Serial
import time

def default_callback():
    pass

class Module(object):

    def __init__(self, callback):
        self.enable()
        self.setCallbackFunction(default_callback)
        self.callback = callback
        self.wakeup_time = None

    def setParent(self, parent):
        self.parent = parent

    def setCallbackFunction(self, function):
        self.callback_function = function

    def executeCallbackFunction(self):
        if self.wakeup_time:
            if time.time() >= self.wakeup_time:
                self.enabled = True
                self.wakeup_time = None

        if self.enabled:
            self.callback_function()

    def enable(self):
        self.enabled = True

    def disable(self, duration = None):
        self.enabled = False

        if duration:
            self.wakeup_time = time.time() + duration
