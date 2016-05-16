from module import Module

class Lever(Module):

    extend_command = "lever_out"
    retract_command = "lever_in"
    state_command = "lever_state"

    def __init__(self, lever_number):
        callback = "L" + str(lever_number) + " pressed"
        self.lever_number = lever_number
        super(Lever, self).__init__(callback)

    def extend(self):
        self.parent.serialWrite(
                Lever.extend_command
                + " "
                + str(self.lever_number)
                + '\n')

        return self.parent.poll()

    def retract(self):
        self.parent.serialWrite(
                Lever.retract_command
                + " "
                + str(self.lever_number)
                + '\n')

        return self.parent.poll()

    def getState(self):
        self.parent.serialWrite(
                Lever.state_command
                + " "
                + str(self.lever_number)
                + '\n')

        return self.parent.poll().split(',')[0] == '1'
