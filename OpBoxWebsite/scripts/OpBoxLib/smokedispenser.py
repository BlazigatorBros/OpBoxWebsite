from module import Module
import time

class SmokeDispenser(Module):

    callback = "SmokeDispenserCallback"
    dose_command = "doses"

    def __init__(self):
        super(SmokeDispenser, self).__init__(SmokeDispenser.callback)

    def dose(self, duration):
        self.parent.serial.write(
                SmokeDispenser.dose_command 
                + " " 
                + str(duration) 
                + '\n'
        )

        time.sleep(duration / 1000.0 * 2)

        return self.parent.poll()
