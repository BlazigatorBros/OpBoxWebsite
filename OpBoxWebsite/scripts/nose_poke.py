import blazigator, logger
from time import *

lg = logger.Logger()
duration = 20

def np_callback():
    lg.log("Nosepoke detected")
    blazigator.eye.disable(3)

blazigator.eye.setCallbackFunction(np_callback)
blazigator.op_box.poll()