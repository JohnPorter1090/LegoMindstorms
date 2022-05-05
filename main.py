#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

motorb=Motor(Port.B, Direction.COUNTERCLOCKWISE)
motorc=Motor(Port.C, Direction.COUNTERCLOCKWISE)
#doormotor = Motor(Port.D)
#ultrasonic = UltrasonicSensor(Port.S1)
colorsensor = ColorSensor(Port.S4)
touchSensorR = TouchSensor(Port.S3) #right
touchSensorL = TouchSensor(Port.S2) #left


robot = DriveBase(motorb, motorc, wheel_diameter=68.8,
axle_track=104)
robot.settings(90000000, 9000000, 5000, 5000)

while True:
    if touchSensorR.pressed() == True and touchSensorL.pressed() == True:
        while touchSensorR.pressed() == True and touchSensorL.pressed() == True:
            robot.straight(-400)
            robot.turn(90)
    elif colorsensor.color() == Color.BLUE:
        while colorsensor.color() == Color.BLUE:
            robot.straight(-400)
            robot.turn(90)
    elif touchSensorR.pressed() == True:
        while touchSensorR.pressed() == True:
            robot.straight(-300)
            robot.turn(180)
    elif touchSensorL.pressed() == True:
        while touchSensorL.pressed() == True:
            robot.straight(-300)
            robot.turn(90)
    else:
        robot.straight(600)
