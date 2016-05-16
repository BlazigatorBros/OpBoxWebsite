from module import Module
import time

class SmokeDispenser(Module):

    callback = "ERROR_SMOKER_EMPTY"
    burn_command = "burn"
    load_command = "load"
    empty_command = "empty"

    def __init__(self):
        super(SmokeDispenser, self).__init__(SmokeDispenser.callback)

    def burn(self):
        self.parent.serialWrite(
                SmokeDispenser.burn_command 
                + '\n'
        )

        return self.parent.poll()

    def load(self):
        self.parent.serialWrite(
                SmokeDispenser.load_command 
                + '\n'
        )

        return self.parent.poll()

    def empty(self):
        self.parent.serialWrite(
                SmokeDispenser.empty_command 
                + '\n'
        )

        return self.parent.poll()
