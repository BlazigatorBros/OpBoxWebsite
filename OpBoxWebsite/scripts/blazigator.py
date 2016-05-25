"""
Contains all modules 
attached to our op box"""

from OpBoxLib.opbox import OpBox
from OpBoxLib.liquiddispenser import LiquidDispenser
from OpBoxLib.smokedispenser import SmokeDispenser
from OpBoxLib.lever import Lever
from OpBoxLib.fan import Fan
from OpBoxLib.eye import Eye
from OpBoxLib.doot import Doot
from OpBoxLib.houselight import Houselight
import time

op_box = OpBox()

liquid_dispenser = LiquidDispenser()
smoke_dispenser = SmokeDispenser()
lever_0 = Lever(0)
lever_1 = Lever(1)
fans = Fan()
eye = Eye()
houselight = Houselight()
doot = Doot()

op_box.attach(liquid_dispenser)
op_box.attach(smoke_dispenser)
op_box.attach(lever_0)
op_box.attach(lever_1)
op_box.attach(fans)
op_box.attach(eye)
op_box.attach(doot)
op_box.attach(houselight)

#give a moment for the serial to attach before issuing commands
time.sleep(1)

if __name__ == "__main__":
	print op_box.debug()
