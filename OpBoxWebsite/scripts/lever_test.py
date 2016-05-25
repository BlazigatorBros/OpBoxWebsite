import logger, blazigator

lg = logger.Logger()
lg.clear()
lg.log(blazigator.op_box.debug())

lg.log("Extending L0")
blazigator.lever_0.extend()
lg.log("Extending L1")
blazigator.lever_1.extend()
lg.log("Retracting L0")
blazigator.lever_0.retract()
lg.log("Retracting L1")
blazigator.lever_1.retract()