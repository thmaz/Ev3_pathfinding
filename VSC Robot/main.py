#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick

from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,

                                 InfraredSensor, UltrasonicSensor, GyroSensor)

from pybricks.parameters import Port, Stop, Direction, Button, Color

from pybricks.tools import wait, StopWatch, DataLog

from pybricks.robotics import DriveBase

from pybricks.media.ev3dev import SoundFile, ImageFile

from pybricks.media.ev3dev import Font



# Create your objects here.

ev3 = EV3Brick()    #ev3

obstacle_sensor = UltrasonicSensor(Port.S4)     #MotionSensor

line_sensor = ColorSensor(Port.S1)





# Initialize the motors

left_motor = Motor(Port.A)

right_motor = Motor(Port.D)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)



#variables
dis = 0
dis1 = 5
dis2 = 7
dis3 = 10

def drive():
  robot.drive_time(-100, 0, 1000)

def obstacle_avoidance():
 wait(2)
 ev3.speaker.beep()

ev3.speaker.say("Place medicine")

wait(5)

while dis < dis1:
      drive()
      dis = dis + 1
      while obstacle_sensor.distance() < 200:
            obstacle_avoidance()

robot.turn(117)

while dis < dis2:
  drive()
  dis = dis + 1
  while obstacle_sensor.distance() < 200:
      obstacle_avoidance()

robot.turn(-117)

while dis < dis3:
  drive()
  dis = dis + 1
  while obstacle_sensor.distance() < 200:
      obstacle_avoidance()

ev3.speaker.say("Done")