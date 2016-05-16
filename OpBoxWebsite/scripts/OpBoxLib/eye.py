from module import Module

class Eye(Module):

    callback = "Beam broken"
    state_command = "beam_state"

    def __init__(self):
        super(Eye, self).__init__(Eye.callback)

    def getState(self):
        self.parent.serialWrite(
                Eye.state_command
                + '\n')

        return self.parent.poll().split(',')[0] == '1'
