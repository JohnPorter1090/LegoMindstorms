from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import time


ev3 = EV3Brick()
motorc=Motor(Port.C) #right
motorb=Motor(Port.B) #left
chainsaw = Motor(Port.D)
robot = DriveBase(motorb, motorc, wheel_diameter=55.5,
axle_track=104)
ev3.speaker.set_speech_options(language='de', voice='m3', speed=10, pitch=50)
ev3.speaker.set_volume(1000)
gyro_sensor = GyroSensor(Port.S2)

xy = y
number = 0
x_value = 0
y _value = 0
gyro_sensor.reset_angle(0)
facingdegrees = gyro.angle()
def reset_gyro():
    gyro_sensor.reset_angle(0)
    while True:
        if gyro_sensor.angle == 0:
            break
    while True:
        if gyro_sensor.speed() == 0:

def gyro_straight(distance):
    target = gyro_sensor.angle()
    gain = 3
    robot.reset()

    while robot.distance() < degrees:
        correction = (target - gyro_sensor.angle())*gain
        robot.drive(distance, correction)
        if xy == x:
            x_value += distance
        elif xy == y:
            y_value += distance


def turn_left(degrees):
    while gyro_sensor.angle > degrees:
        motorb.run(100)
    motorb.stop()
    xy = 


def turn_right(degrees):
    while gyro_sensor.angle > degrees:
        motorc.run(100)
    motorc.stop()
    number += 1
    if number % 2 == 0:
        xy = x
    elif number % 2 == 1:
        xy = y
    if d

def go_to_zero_zero():
    target = gyro_sensor.angle()
    gain = 3
    robot.reset()
    correction = (target - gyro_sensor.angle())*gain
    if xy = y:
        robot.drive(-y_value, correction)
        y_value = 0
        turn_left()
        robot.drive(-x_value,correction)
        x_value = 0
    elif xy = x:
        robot.drive(-x_value, correction)
        x_value = 0
        turn_left()
        robot.drive(-y_value,correction)
        y_value = 0

turn_right(90)


while True:
    gyro_straight(100)
    