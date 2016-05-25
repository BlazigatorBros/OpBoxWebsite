from module import Module

class Doot(Module):
    """
Speaker controll
    """

    callback = "DootCallback"
    set_doot_command = "set_doot"
    doot_command = "doot"

    def __init__(self):
        super(Doot, self).__init__(Doot.callback)

    def set(self, hz):
        """
Set dooter frequency

Arguments:
hz -- desired doot frequency
        """
        self.parent.serialWrite(
                Doot.set_doot_command
                + " "
                + str(hz)
                + '\n')

        return self.parent.poll()

    def doot(self, duration):
        """
DOOT DOOOO

Arguments:
duration -- desired doot duration
        """
        self.parent.serialWrite(
                Doot.doot_command
                + " "
                + str(duration)
                + '\n')

        return self.parent.poll()
