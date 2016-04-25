from module import Module

class LiquidDispenser(Module):

    callback = "LiquidDispenserCallback"
    dispense_command = "disp"

    def __init__(self):
        super(LiquidDispenser, self).__init__(LiquidDispenser.callback)

    def dispense(self, duration):
        self.parent.serial.write(
                LiquidDispenser.dispense_command 
                + " " 
                + str(duration)
                + '\n')

        return self.parent.poll()
