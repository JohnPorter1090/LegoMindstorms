from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import time


ev3 = EV3Brick()
motorc=Motor(Port.B) #right
motorb=Motor(Port.C) #left
chainsaw = Motor(Port.D)
robot = DriveBase(motorb, motorc, wheel_diameter=55.5,
axle_track=104)
ev3.speaker.set_speech_options(language='de', voice='m3', speed=10, pitch=50)
ev3.speaker.set_volume(1000)
gyro_sensor = GyroSensor(Port.S2)

"""
Gameplan:





"""
xy = "y"
number = 0


x_value = 0
y_value = 0

"""
among = 1
while True:
    print("Patching Ticket #" + among)
    among = among + among
"""

gyro_sensor.reset_angle(0)



directional_degrees = 0

def get_correct_angle(directional_degrees):
    if directional_degrees == 360:
        directional_degrees = 0
    elif directional_degrees == -90:
        directional_degrees = 270
    elif directional_degrees == 450:
        directional_degrees = 90
    elif directional_degrees == -180:
        directional_degrees = 180

while True:
    ev3.speaker.beep(frequency=1000,duration=500)
    ev3.speaker.beep(frequency=750 ,duration=500)

def reset_gyro():
    gyro_sensor.reset_angle(0)
    while True:
        if gyro_sensor.angle() == 0:
            break
    while True:
        if gyro_sensor.speed() == 0:
            break
def gyro_straight(distance, x_coord, y_coord):
    target = gyro_sensor.angle()
    gain = 3
    robot.reset()
    while robot.distance() < distance:
        correction = (target - gyro_sensor.angle())*gain
        robot.drive(distance, correction)
        if xy == "x":
            x_coord += distance
        elif xy == "y":
            y_coord += distance


def turn_left(degrees, number, directional_degrees):
    while gyro_sensor.angle() > degrees:
        motorb.run(degrees)
    motorb.stop()
    number += 1
    directional_degrees += 90
    get_correct_angle(directional_degrees)
    if number % 2 == 1:
        xy = "x"
    elif number % 2 == 0:
        xy = "y"
    


def turn_right(degrees, number, directional_degrees):
    while gyro_sensor.angle() > degrees:
        motorc.run(degrees)
    motorc.stop()
    number += 1
    directional_degrees -= degrees
    get_correct_angle(directional_degrees)
    if number % 2 == 1:
        xy = "x"
    elif number % 2 == 0:
        xy = "y"

# Directional_Degrees
# 0 facing  N   Y
# 90 facing  E   X
# 180 facing  S   Y
# 270 facing   W   X

def go_to_coordinate(direction, x_coord, y_coord, directional_degrees):
    while directional_degrees != direction:
        turn_right(90)
        directonal_degrees -= 90
        get_correct_angle(directional_degrees)
    if xy == "y":
        robot.drive(y_coord, correction)
        y_value = y_coord
        turn_left(90, number)
        robot.drive(x_coord,correction)
        x_value = x_coord
    elif xy == "x":
        robot.drive(x_coord, correction)
        x_value = x_coord
        turn_left(90, number)
        robot.drive(y_coord,correction)
        y_value = y_coord
    
    
    
    """
                                                                                    
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                           ,***,,,,,,,,,,,,,,,*//.                              
                      /,,,,*******************,,,,,,,*          ......          
                ..*,,,,******************************,,,,. . ...........        
           .//////*//***********************************,,*...............      
          (   .(/*/////*/////***,**,,....,,****************,*,,,,,,,,,...,      
         .       ///((/((///,,//////..,,**********************,,,**,,,,,.,.     
        .*/@     ./        (/////////*************************/*******,,..      
       .,,@@         .       ////////////****************////*//*((((,,...      
       ,(&@      . # %&.      ///////////////////////////////////((,,,...       
       *..      ..%&&&@       ,////////////////////////////////((/*,,..,        
       *,,.   .(...&&(        (//////////////////////////////((((/,,...         
       ,,,,,....,..          ////////////////////////////((((((((*..,           
       .,,,,.....,,...     .     ,/(/////////////////(/((((((((((,              
        ,,*,,........... .               *(///((((((((((((((((((.               
          ,,*,................                 /(((((((((((((((                 
           .*,,*****/,.      ..                   . (((((((((*                  
              *****,,,,................................((((,                    
                 *********,,,,,,,,,............,,,,,,,,/.                       
                     .*****************,,,,,,,******                            
                             .,************..                                   
                                                                                
                                                                                 
                                                                                
                                                                                
                                                                                
    """


def go_to_zero_zero(target):
    target = 270
    gain = 3
    robot.reset() 
    correction = (target - gyro_sensor.angle())*gain
    if xy == "y":
        robot.drive(-y_value, correction)
        y_value = 0
        turn_left()
        robot.drive(-x_value,correction)
        x_value = 0
    elif xy == "x":
        robot.drive(-x_value, correction)
        x_value = 0
        turn_left()
        robot.drive(-y_value,correction)
        y_value = 0

reset_gyro()
print(directional_degrees)
turn_right(90, number, directional_degrees)
turn_left(180, number, directional_degrees)

print(directional_degrees)


"""
while True:
    gyro_straight(100, x_value, y_value)
"""


