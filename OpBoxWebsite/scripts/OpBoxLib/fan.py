from module import Module

class Fan(Module):

    callback = "FanCallback"
    get_speed_command = "get_speed"
    set_speed_command = "set_speed"

    def __init__(self):
        super(Fan, self).__init__(Fan.callback)

    def setSpeed(self, rpm):
        self.parent.serialWrite(
                Fan.set_speed_command
                + " "
                + str(rpm)
                + '\n')

        return self.parent.poll()

    def getSpeed(self):
        self.parent.serialWrite(
                Fan.get_speed_command
                + '\n')

        return int(self.parent.poll().split(',')[0])
