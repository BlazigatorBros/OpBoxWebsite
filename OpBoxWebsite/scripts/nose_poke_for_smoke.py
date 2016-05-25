import logger, blazigator

lg = logger.Logger()
lg.clear()

def dispenseSmoke():

	lg.log("Nosepoke Detected")
	blazigator.eye.disable(3)
	lg.log("Dispencing Smoke")
	lg.log(blazigator.smoke_dispenser.burn())

lg.log(blazigator.smoke_dispenser.load())
blazigator.eye.setCallbackFunction(dispenseSmoke)
blazigator.op_box.poll()