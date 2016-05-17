from module import Module

class LiquidDispenser(Module):
    """
Retuns liquid reward dispencer solinoid
    """

    callback = "LiquidDispenserCallback"
    dispense_command = "disp"

    def __init__(self):
        super(LiquidDispenser, self).__init__(LiquidDispenser.callback)

    def dispense(self, duration):
        """
Opens liquid reward solinoid for a set ammount of time

Argumrnts:
duration -- amount of time (ms) that solinoid remains open
        """
        self.parent.serialWrite(
                LiquidDispenser.dispense_command 
                + " " 
                + str(duration)
                + '\n')

        return self.parent.poll()
