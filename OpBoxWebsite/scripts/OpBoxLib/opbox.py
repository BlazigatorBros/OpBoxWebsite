import time
from serial import Serial

class OpBox:
    """
        Represents the op-box controller and the collection of modules attached to it
    """

    port = "/dev/ttyACM0"
    baudrate = 9600

    def __init__(self):

        self.serial = Serial(OpBox.port, OpBox.baudrate)
        self.modules = []
	self.callbacks = {}

    def waitForModule(self, *modules):
        """
        polls untill one of the modules callbacks are called
        """

        callbacks = [m.callback for m in modules]

        #get next response that is not from an interupt
	while(True):
                response = self.serial.readline()
                if(self.callback(response)):
        	        if response.split(",")[0] in callbacks:
                                return

    def poll(self):
        """
        returns the next line read from the serial port
        who is not assoicated with a callback function
        executing relivant callbacks along the way.
        """

        #get next response that is not from an interupt
	response = self.serial.readline()
        while(self.callback(response)):
        	response = self.serial.readline()

	return response

    def debug(self):
	"""
	Returns debug information
	"""

        self.serialWrite("debug\n")
	return self.poll()

    def attach(self, module):
	"""
	attach a new module to the box
	"""

        module.setParent(self)
        self.modules.append(module)
        self.callbacks[module.callback] = module.executeCallbackFunction

    def callback(self, response):
	"""
	go through the list of callbacks and execute if applicable
	"""

        command = response.split(",")[0]
        if command in self.callbacks.keys():
            self.callbacks[command]()
            return True
        else: return False

    def serialWrite(self, command):
            time.sleep(.2)
            self.serial.setDTR(level=1) 
            time.sleep(.2)
            self.serial.write(command)

    def getTimestamp(self):

        self.serialWrite("time\n")
        return int(self.poll())
