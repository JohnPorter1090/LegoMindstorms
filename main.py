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
robot.settings(500000000, 5000000, 5000, 5000)

count = 0
"""  
while count % 2 == 0:
    ev3.screen.print(*"Middle: Initialized")
    if ultrasonic.distance() > 1000:
        ev3.screen.print(*str(ultrasonic.distance()))
        #doormotor.run_target(1000, 1000)
        robot.turn(180)
        count += 1
    else:
        robot.straight(400)
        ev3.screen.print(*"Middle: Moving Forward")

while count % 2 != 0:
    ev3.screen.print(*"Goal: Initialized")

    if ultrasonic.distance() > 900 and colorsensor.color() == Color.RED:
        ev3.screen.print(*str(ultrasonic.distance()))
        ev3.screen.print(*str(colorsensor.color()))
        #door.run_target(-1000, 1000)
        robot.straight(-500)
        robot.turn(180)
        count += 1
    else:
        ev3.screen.print(*str(ultrasonic.distance()))
        ev3.screen.print(*str(colorsensor.color()))
        robot.straight(400)
        ev3.screen.print(*"Goal: Moving Forward")
        
"""
middleLoop = True
goalLoop = True

robot.straight(500)

while middleLoop:
    if ultrasonic.distance() > 500:
        robot.turn(180)
        middleLoop = False
    else:
        robot.straight(20)

robot.straight(500)
while goalLoop:
    if touchSensorR.buttonpressed() == True:
        robot.straight(-100)
        robot.turn(90)
    if touchSensorL.buttonpressed() == True:
        robot.straight(-100)
        robot.turn(-90)

    if ultrasonic.distance() > 500:
        robot.straight(-100)
        robot.turn(180)
    else:
        robot.straight(20)
