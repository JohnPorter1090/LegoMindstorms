#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

motorb=Motor(Port.B)
motorc=Motor(Port.C)
#doormotor = Motor(Port.D)
ultrasonic = UltrasonicSensor(Port.S1)
colorsensor = ColorSensor(Port.S4)
touchSensorR = TouchSensor(Port.S3) #right
touchSensorL = TouchSensor(Port.S2) #left


robot = DriveBase(motorb, motorc, wheel_diameter=68.8,
axle_track=104)
robot.settings(9000, 9000, 5000, 5000)

while True:
    if touchSensorR.pressed() == True and touchSensorL.pressed() == True:
        while touchSensorR.pressed() == True and touchSensorL.pressed() == True:
            robot.straight(-400)
            robot.turn(90)
    elif colorsensor.color() == Color.RED:
        while colorsensor.color() == Color.RED:
            robot.straight(-400)
    elif ultrasonic.distance() < 200:
        while ultrasonic.distance() < 200:
            robot.straight(-400)
    elif touchSensorR.pressed() == True:
        while touchSensorL.pressed() == True:
            robot.straight(-300)
            robot.turn(180)
    elif touchSensorL.pressed() == True:
        while touchSensorL.pressed() == True:
            robot.straight(-300)
            robot.turn(180)
    else:
        robot.straight(200)
