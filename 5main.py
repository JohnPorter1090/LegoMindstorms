#!/usr/bin/env pybricks-micropython
'''
What we'll do:
0a. Make sure door open
1. Book it forward into the other robot
2. Close door, turn around
3. Move back to goal and deposit
 a.
 b.
 c. 
4. Down and back cycle
5. Maybe like drive into opponent goal at end...? 
-
What we need:
-Move straight
-Turn

Sesnors:
-Ultrasonic forward
-Touch back
'''



from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()


motorc=Motor(Port.B)
motorb=Motor(Port.C)
touchsensor = TouchSensor(Port.S3)
robot = DriveBase(motorb, motorc, wheel_diameter=68.8,
axle_track=104)
distance = 700

speed = 250

"""
robot.settings(1000, 1000, 1000, 1000)
"""

ev3.speaker.set_speech_options(language='de', voice='m3', speed=10, pitch=50)
ev3.speaker.set_volume(1000)
gyro_sensor = GyroSensor(Port.S2) # +/- 3 degrees
door = Motor(Port.D)
ears = UltrasonicSensor(Port.S1)
color_sensor = ColorSensor(Port.S4)

#1400 180 degrees
gyro_sensor.reset_angle(0)

if distance > 0:
    while robot.distance() <= distance():
        turn_power = 0 - gyro_sensor.angle()
        correction = turn_power*2.5
        robot.drive(250, correction)
    robot.stop()
    motorc.brake()
    motorb.brake()
else:
    while robot.distance() <= distance():
        turn_power = 0 - gyro_sensor.angle()
        correction = turn_power*2.5
        robot.drive(-250, correction)
    robot.stop()
    motorc.brake()
    motorb.brake()



"""
def perfect_straight(distance):
    
    
    
def perfect_turn(degrees):
    translated_degrees = degrees/7.77777
    forward = gyro_sensor.angle()
    target = 
    
    robot.turn(translated_degrees)
    if gyro_sensor.angle()
    


"""