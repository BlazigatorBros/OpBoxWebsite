from serial import Serial

class Module(object):

    def default_callback():
        pass

    def __init__(self, callback):
        self.enable()
        self.setCallbackFunction(Module.default_callback)
        self.callback = callback
        self.wakeup_time = None

    def setParent(self, parent):
        """
        assigns an OpBox instance to this module

        Arguments:
        parent -- the OpBox instance this module is attached to
        """
        self.parent = parent

    def setCallbackFunction(self, function):
        """
        sets the callback function to be called when this module is interacted with

        Arguments:
        function -- callback function
        """
        self.callback_function = function

    def executeCallbackFunction(self):
        """
        if this module is enabled, the callback function will be executed.

        Arguments: None
        """

        if self.wakeup_time:
            if time.time() >= self.wakeup_time:
                self.enabled = True
                self.wakeup_time = None

        if self.enabled:
            self.callback_function()

    def enable(self):
        """
        Overide disable timer and enable module now

        Argurments: None
        """
        self.enabled = True

    def disable(self, duration = None):
        """
        Disables callback function, if duration is given, module is re-enabled after a set amout of time

        Arguments:
        duration -- default value: None
                if this is a number, the module is enabled after this much time (sec)  has passed
        """
        self.enabled = False

        if duration:
            self.wakeup_time = time.time() + duration
