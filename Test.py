from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import time

ev3 = EV3Brick()
motorc=Motor(Port.C) #right
motorb=Motor(Port.B) #left
chainsaw = Motor(Port.D)

chainsaw.run_time(1000, 1000)