#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import time


count = 0
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

"""
Link to the Pybricks commands:
https://pybricks.com/ev3-micropython/hubs.html#pybricks.hubs.EV3Brick.buttons.pressed

#https://education.lego.com/en-us/product-resources/mindstorms-ev3/downloads/building-instructions
def move():
"""

# Create your objects here.
ev3 = EV3Brick()
motorc=Motor(Port.C)
motorb=Motor(Port.B)
chainsaw = Motor(Port.D)
robot = DriveBase(motorb, motorc, wheel_diameter=55.5,
axle_track=104)
ev3.speaker.set_speech_options(language='de', voice='m3', speed=10, pitch=50)
ev3.speaker.set_volume(1000)

obstacle_sensor = UltrasonicSensor(Port.S4)
color_sensor = ColorSensor(Port.S2)
touch1 = TouchSensor(Port.S1)
touch3 = TouchSensor(Port.S3)
"""
ev3.speaker.say("Auf der Heide blüht ein kleines Blümelein und das heißt: ErikaHeiß von hunderttausend kleinen Bienelein wird umschwärmt Erika, denn ihr Herz ist voller Süßigkeit, zarter Duft entströmt dem Blütenkleid. Auf der Heide blüht ein kleines Blümelein und das heißt: Erika.")
"""
"""
ev3.speaker.play_file("Vine-boom-sound-effect (1).wav")
"""
def amogus():
    ev3.speaker.play_notes(['C4/5', 'D#4/5', 'F4/5', 'F#4/5', 'F4/5', 'D#4/5', 'C4/5',],tempo=120)
    wait(750)
    ev3.speaker.play_notes(['A#3/6', 'D4/6', 'C4/3'], tempo=120)
def better_off_alone():
    ev3.speaker.play_notes(['B4/5', 'B4/5', 'G#4/5', 'B4/5', 'B4/5', 'A#4/5', 'F#3/6', 'F#5/5', 'F#5/5', 'D#5/5', 'B4/5', 'B4/5', 'G#4/5', 'B4/5', 'B4/5', 'A#4/5', 'F#4/6', 'D#5/5', 'E#5/5', 'D#5/5'],tempo=137)

def sing():
    ev3.screen.print("AMOGUS")
    amogus()
    ev3.screen.clear()
    ev3.screen.print("You're in for a")
    ev3.screen.print("bad time")
    ev3.screen.print("2nd AMEND.")
    wait(750)
    ev3.speaker.play_notes(['D4/6', 'D4/6', 'D5/6', 'A4/4', 'G#4/5', 'G4/5', 'F4/6', 'D4/6', 'F4/6', 'G4/4'],tempo=120)
    wait(750)
def go_forth_forever():
    while True:
        color = color_sensor.color()
        if color.Black:
            amogus()
            robot.drive(-1000,0)
        robot.drive(1000, 0)
        chainsaw.run_time(2000,1000)
        if touch1.pressed() or touch3.pressed():
            ev3.speaker.beep(frequency=500, duration=100)
            robot.straight(-100)
            ev3.speaker.beep(frequency=500, duration=100)
            robot.turn(105)
            ev3.speaker.beep(frequency=500, duration=100)
        if obstacle_sensor.distance() < 350:
            robot.straight(-50)
            ev3.speaker.beep(frequency=500,duration=500)
            robot.turn(105)



def activate_chainsaw():
    while True:
        chainsaw.run_target(500,-360)
def cut_through_obstacle():
    if obstacle_sensor.distance() < 500:
        chainsaw.run_time(2000,1000)
    elif obstacle_sensor.distance() < 350:
            robot.straight(-50)
            ev3.speaker.beep(frequency=500,duration=500)
            amogus()
            robot.turn(105)
def go_forth():
    robot.straight(1000)
    robot.turn(210)
    robot.straight(2000)

def move():
    motorb.run_target(500,-360)
    motorc.run_target(500,-360)
    motorb(positive_direction=Direction.CLOCKWISE)
    ev3.speaker.play_file(SoundFile.STOP)
    robot.turn(360)

"""
go_forth()
sing()
better_off_alone()
"""

go_forth_forever()
cut_through_obstacle()