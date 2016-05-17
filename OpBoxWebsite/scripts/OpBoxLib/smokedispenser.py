from module import Module
import time

class SmokeDispenser(Module):
    """
    controlls smoke emitter
    """

    callback = "ERROR_SMOKER_EMPTY"
    burn_command = "burn"
    load_command = "load"
    empty_command = "empty"

    def __init__(self):
        super(SmokeDispenser, self).__init__(SmokeDispenser.callback)

    def burn(self):
        """
        burn a loaded pellit and load the next one. The animal gets lit #420swaggg

        Arguments: None
        """
        self.parent.serialWrite(
                SmokeDispenser.burn_command 
                + '\n'
        )

        return self.parent.poll()

    def load(self):
        """
        load the next pellit to be burned

        Arguments: None
        """
        self.parent.serialWrite(
                SmokeDispenser.load_command 
                + '\n'
        )

        return self.parent.poll()

    def empty(self):
        """
        empty all pellits in chute

        Arguments: None
        """
        self.parent.serialWrite(
                SmokeDispenser.empty_command 
                + '\n'
        )

        return self.parent.poll()
