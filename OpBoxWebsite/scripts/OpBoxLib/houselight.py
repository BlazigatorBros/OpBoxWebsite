from module import Module

class Houselight(Module):
    """
Exaust fan controll
    """

    callback = "HouselightCallback"
    set_light_command = "houselight"

    def __init__(self):
        super(Houselight, self).__init__(Houselight.callback)

    def set(self, state):
        """
Set houselight on or off

Arguments:
state -- desired state of light
        """
        self.parent.serialWrite(
                Houselight.set_light_command
                + " "
                + str(int(state))
                + '\n')

        return self.parent.poll()
