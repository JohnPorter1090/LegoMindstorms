#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()








"""
Gameplan:


1. Robot is always at a set angle
2. If detects offset, it gets back in line
3. Start in bottom right corner/ top left corner
4. Start by going forward
5. When color sensor detects other side of arena, continues to move forward for a few seconds, closes box and moves backwards to go home
6. Ultrasonic on back detects back wall and starts the goal dropoff sequence once certain distance-FIND THIS DISTANCE WITH TEST to see when turn 
    if whole robot + cap holder will stay in goal (check that against movement values of location to see if there is another robot)
7. Drop off sequence: Check floor for correct color, then turn 90 drive to far end and open box, back up and continue sequence of picking up caps
8. Maybe something cool at end like steal caps, like:
    -at end bulldoze other teams goal

-Touch in front if robot detected goes to ultrasonic in back to get position
-Upon robot detected, do something (ram into maybe) and then leave using ultrasonic for position

"""
motorc=Motor(Port.B) #right
motorb=Motor(Port.C) #left
touchsensor = TouchSensor(Port.S3)
robot = DriveBase(motorb, motorc, wheel_diameter=55.5,
axle_track=104)
ev3.speaker.set_speech_options(language='de', voice='m3', speed=10, pitch=50)
ev3.speaker.set_volume(1000)
gyro_sensor = GyroSensor(Port.S2)
door = Motor(Port.A)
ears = UltrasonicSensor(Port.D)
color_sensor = ColorSensor(Port.S1)

gyro_sensor.reset_angle(0)



base_side_color = color_sensor.color()


 goal_color = color.RED # SET GOAL COLOR HERE SET GOAL COLOR HERE SET GOAL COLOR HERE SET GOAL COLOR HERE

if goal_color == color.RED:
    apponent_color = color.BLUE
else:
    apponent_color = color.RED



door_position = ("open")
#
#

def absolute_straight(distance):
    while True:
        if gyro_sensor.angle() <= 5 and gyro_sensor.angle() >= -5:
            robot.straight(distance)
            break
        elif gyro_sensor.angle() < 180 and gyro_sensor.angle() > 5:
            robot.turn(10)
            print("straight: angle too low")
            screen.print("straight: angle too low")
        elif gyro_sensor.angle() > 180 or gyro_sensor.angle() < -5:
            robot.turn(-10)
            print("straight: angle too high")
            screen.print("straight: angle too high")
        elif gyro_sensor.angle() == 180:
            robot.turn(180)

def absolute_turn(degrees):
    margine_of_error = 2
    turning_degrees = 0
    starting_gyro_degrees = gyro_sensor.angle()


    while True:
        turning_degrees = gyro_sensor.angle() - starting_gyro_degrees
        print(turning_degrees)
        screen.print(turning_degrees)
        if turning_degrees > degrees - margine_of_error or turning_degrees < degrees + margine_of_error
            break


        elif turning_degrees > degrees:
            robot.turn(-10)
        elif turning_degrees < degrees:
            robot.turn(10)
        
        
        
#
#



def distance(millimeters): #converts distance in mm to 1/4 in
    distance_value = ((millimeters/25.4)/4)
    return distance_value

x = 0
y = 0 

def deposit_bottlecaps():


def go_to_middle(base_side_color):
    while True:
        if color_sensor.color() = base_side_color:
            absolute_straight():
        elif color_sensor.color() != base_side_color:
            absolute_turn(90)
            break

"""
"""
def collect_bottle_caps():
    distance_to_wall = 1000
    door_close_time = 150
    absolute_straight(distance_to_wall)
    door.run_time(1000, door_close_time)
""""""
def turn_on_buttonpress():
    if touchsensor.pressed():
        robot.straight(30)
        robot.straight(-300)
        while gyro_sensor.angle() < 180 or gyro_sensor.angle() < -180:
            robot.turn(-10)
            print("button: low")
            screen.print("button: low")
        while gyro_sensor.angle() > 180 or gyro_sensor.angle() > -180:
            robot.turn(10)
            print("button: high")
            screen.print("button: high")
        gyro_sensor.reset_angle(0)
        print("button: angle reset")
        screen.print("button: angle reset")
""""""
def return_to_goal():
    absolute_turn(90)
    absolute_straight(1000)
    while True:
        if ears.distance() <= 50:
            absolute_turn(90)
            break
        else:
            absolute_straight(30)

def go_to_apponents_goal():
    absolute_turn(-90)
    absolute_straight(-1000)
    while True:
        if ears.distance() <= 50:
            absolute_turn(-90)
            break
        else:
            absolute_straight(-30)


def deposit_on_goal(door_position):
    while True:
        




    

go_to_middle(base_side_color)

    
    
    