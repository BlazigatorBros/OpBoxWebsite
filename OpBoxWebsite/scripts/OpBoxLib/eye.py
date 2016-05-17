from module import Module

class Eye(Module):
    """
Breakbeam sensor
    """

    callback = "Beam broken"
    state_command = "beam_state"

    def __init__(self):
        super(Eye, self).__init__(Eye.callback)

    def getState(self):
        """
check state of breakbeam 
and return true if broken

Arguments: None
        """
        self.parent.serialWrite(
                Eye.state_command
                + '\n')

        return self.parent.poll().split(',')[0] == '1'
