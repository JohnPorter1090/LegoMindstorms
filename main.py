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

#
#
# add a function here that inputs a turn angle and makes a perfect turn
#
#

gyro_sensor.reset_angle(0)

init_color = color_sensor.color() #Detects the color of the goal for the side that the robot is on


def distance(millimeters): #converts distance in mm to 1/4 in
    distance_value = ((millimeters/25.4)/4)
    return distance_value

x = 0
y = 0 

def absolute_straight():
        if gyro_sensor.angle() <= 5 and gyro_sensor.angle() >= -5:
            robot.straight(300)
            door.run_time(-1000, 300)
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

def deposit_bottlecaps(goalcolor):
    if color_sensor.color() == goalcolor:
        if ears.distance() <= 100:
            door.run_time(-1000, 500)
        elif ears.distance > 100:
            robot.turn(180)
        else:
            robot.turn(180)



while True:
    turn_on_buttonpress()
    absolute_straight()
    deposit_bottlecaps(init_color)

    
    
    