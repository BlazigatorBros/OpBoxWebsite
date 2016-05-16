from serial import Serial

class Module(object):

    def default_callback():
        pass

    def __init__(self, callback):
        self.enable()
        self.setCallbackFunction(Module.default_callback)
        self.callback = callback

    def setParent(self, parent):
        self.parent = parent

    def setCallbackFunction(self, function):
        self.callback_function = function

    def executeCallbackFunction(self):
        if self.enabled:
            self.callback_function()

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False
