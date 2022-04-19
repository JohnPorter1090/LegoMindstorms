from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import time








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

ev3 = EV3Brick()
motorc=Motor(Port.B) #right
motorb=Motor(Port.C) #left
touchsensor = TouchSensor(Port.S3)
robot = DriveBase(motorb, motorc, wheel_diameter=55.5,
axle_track=104)
ev3.speaker.set_speech_options(language='de', voice='m3', speed=10, pitch=50)
ev3.speaker.set_volume(1000)
gyro_sensor = GyroSensor(Port.S2)


gyro_sensor.reset_angle(0)

def distance(millimeters): #converts distance in mm to 1/4 in
    

x =  0
y = 0 

def absolute_straight():
        if gyro_sensor.angle() <= 1 and gyro_sensor.angle() >= -1:
            robot.straight(10)
        elif gyro_sensor.angle() < 180 and gyro_sensor.angle() > 1:
            robot.turn(1)
            print("angle too low")
        elif gyro_sensor.angle() > 180 or gyro_sensor.angle() < -1:
            robot.turn(-1)
            print("angle too high")
        elif gyro_sensor.angle() == 180:
            robot.turn(180)


def turn_on_buttonpress():
    if touchsensor.pressed():
        robot.straight(-300)
        while gyro_sensor.angle() < 180 or gyro_sensor.angle() < -180:
            robot.turn(-10)
            print("low")
        while gyro_sensor.angle() > 180 or gyro_sensor.angle() > -180:
            robot.turn(10)
            print("high")
        gyro_sensor.reset_angle(0)
        print("angle reset")
while True:
    turn_on_buttonpress()
    absolute_straight()