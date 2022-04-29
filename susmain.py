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

Senors:
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

robot.settings(1000, 1000, 1000, 1000)


ev3.speaker.set_speech_options(language='de', voice='m3', speed=10, pitch=50)
ev3.speaker.set_volume(1000)
gyro_sensor = GyroSensor(Port.S2) # +/- 3 degrees
door = Motor(Port.D)
ears = UltrasonicSensor(Port.S1)
color_sensor = ColorSensor(Port.S4)


#Debugging Zone

abs_stra_margin = 5 
abs_stra_movement_checking = 150 #distance in mm

abs_turn_margin = 5

door_time = 1000 

# 1400 = 180 degrees
#ttt

def absolute_straight(distance):
    

            

def absolute_turn(turn_amount):
    
    destination = gyro_sensor.angle() + turn_amount 
    robot.turn(turn_amount)    
    
    while True:
        if gyro_sensor.angle() == destination:
            print("Abs_Turn: Successfully Turned Correct Distance")
            break

        if gyro_sensor.angle() > destination + abs_turn_margin: #Angle is more to the right
            print("Abs_Turn: Angle is too far to the right. Current: " + str(gyro_sensor.angle()) + " Target: " + str(destination))
            robot.turn(-1)
            
        elif gyro_sensor.angle() < destination - abs_turn_margin: #Angle is more to the left
            print("Abs_Turn: Angle is too far to the left. Current: " + str(gyro_sensor.angle()) + " Target: " + str(destination))
            robot.turn(1)
        
        else:
            print("Abs_Turn: Error in absolute turning")
         
        
    
    

def open_door():
    door.run_time(1000, door_time)


def close_door():
    door.run_time(-1000, door_time)



gyro_sensor.reset_angle(0)


#Enter Movement Pattern Here
#absolute_straight(1200)
#absolute_straight(-100)
#absolute_turn(180)
#absolute_straight(1100)

robot.straight(-5000)
robot.turn(1400)
robot.straight(-5000)
robot.turn(-1400)