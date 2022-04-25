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


#!/usr/bin/env pybricks-micropython
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
robot = DriveBase(motorb, motorc, wheel_diameter=55.5, #FIX THE WHEEL DIAMETER PLEASE PLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASEPLEASE
axle_track=104)
ev3.speaker.set_speech_options(language='de', voice='m3', speed=10, pitch=50)
ev3.speaker.set_volume(1000)
gyro_sensor = GyroSensor(Port.S2) # +/- 3 degrees
door = Motor(Port.D)
ears = UltrasonicSensor(Port.S1)
color_sensor = ColorSensor(Port.S4)

#Debugging Zone
abs_stra_margin = 1 
abs_stra_movement_checking = 10 #distance in mm

abs_turn_marign = 1

door_time = 1000

def absolute_straight(distance):
    
    straight = gyro_sensor.angle()
    distance_traveled = 0
    
    while True:
        if distance_traveled >= distance:
            print("Abs_Straight: Successfully Traveled Desired Distance")
            break

        if gyro_sensor.angle() > straight + abs_stra_margin: # Angle is more to the right
            print("Abs_Straight: Angle is too far to the right. Current: " + gyro_sensor.angle() + " Target: " + straight)
            robot.turn(-1)
            
        elif gyro_sensor.angle() < straight - abs_stra_margin: # Angle is more to the left
            print("Abs_Straight: Angle is too far to the left. Current: " + gyro_sensor.angle() + " Target: " + straight)
            robot.turn(1)
            
        else:
            print("Abs_Straight: Angle is perfect, continuing course")
            robot.straight(abs_stra_movement_checking)
            distance_traveled += abs_stra_movement_checking
            

def absolute_turn(turn_amount):
    
    destination = gyro_sensor.angle() + turn_amount 
    robot.turn(turn_amount)    
    
    while True:
        if gyro_sensor.angle() == destination:
            print("Abs_Turn: Successfully Turned Correct Distance")
            break

        if gyro_sensor.angle() > destination + abs_turn_margin: #Angle is more to the right
            print("Abs_Turn: Angle is too far to the right. Current: " + gyro_sensor.angle() + " Target: " + destination)
            robot.turn(-1)
            
        elif gyro_sensor.angle() < destination - abs_turn_margin: #Angle is more to the left
            print("Abs_Turn: Angle is too far to the left. Current: " + gyro_sensor.angle() + " Target: " + destination)
            robot.turn(1)
        
        else:
            print("Abs_Turn: Error in absolute turning")
         
        
    
    

def open_door():
    door.run_time(1000, door_time)


def close_door():
    door.run_time(-1000, door_time)



gyro_sensor.reset_angle(0)


#Enter Movement Pattern Here
absolute_straight(1200)
close_door()
absolute_straight(-100)
absolute_turn(180)
absolute_straight(1100)
open_door()


_sensor.reset_angle(0)


#Enter Movement Pattern Here
absolute_straight(1200)
close_door()
absolute_straight(-100)
absolute_turn(180)
absolute_straight(1100)
open_door()


