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
door = Motor(Port.D)
ears = UltrasonicSensor(Port.S1)
color_sensor = ColorSensor(Port.S4)



gyro_sensor.reset_angle(0)



goal_color = Color.RED # SET GOAL COLOR HERE SET GOAL COLOR HERE SET GOAL COLOR HERE SET GOAL COLOR HERE

if goal_color == Color.RED:
    apponent_color = Color.BLUE
else:
    apponent_color = color.RED



#

def absolute_straight(distance):
    while True:
        if gyro_sensor.angle() <= 5 and gyro_sensor.angle() >= -5:
            robot.run_time(1000, distance*10)
            print("Straight: Succesfully Moved Distance")
            break
        elif gyro_sensor.angle() < 180 and gyro_sensor.angle() > 5:
            robot.turn(10)
            print("Straight: angle too low. Current: " + gyro_sensor.angle())
        elif gyro_sensor.angle() > 180 or gyro_sensor.angle() < -5:
            robot.turn(-10)
            print("Straight: angle too high. Current: " + gyro_sensor.angle())
        elif gyro_sensor.angle() == 180:
            robot.turn(180)
            print("Straight: Robot is facing the opposite direction, attempting correction...")


def absolute_turn(degrees):
    margine_of_error = 2
    turning_degrees = 0
    starting_gyro_degrees = gyro_sensor.angle()


    while True:
        turning_degrees = gyro_sensor.angle() - starting_gyro_degrees
        print("Current: " + turning_degrees + " Target: " + degrees) 
        #screen.draw_text(turning_degrees)
        if turning_degrees > degrees - margine_of_error or turning_degrees < degrees + margine_of_error:
            break
        print("Turn completed")


        elif turning_degrees > degrees:
            robot.turn(-10)
            print("Turn: angle of degrees is too high. Current Value: " + turning_degrees + " Target: " + degrees)
        elif turning_degrees < degrees:
            robot.turn(10)
            print("Turn: angle of degrees is too low. Current Value: " + turning_degrees + " Target: " + degrees)



#WARNING THESE VALUES HAVE NOT BEEN TESTED
#ROBOT MUST BE MONITORED WHILST OPERATING

absolute_straight(2425)
door.run_time(-1000, 2000)
absolute_turn(180)
absolute_straight(2425)
door.run_time(1000, 2000)


    
    