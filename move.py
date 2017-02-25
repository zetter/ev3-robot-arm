# Step 1.9 Moving the motors
# https://www.futurelearn.com/courses/build-a-robot-arm/1/steps/154170

import time

import ev3dev.ev3 as ev3
import ev3dev.fonts as fonts
import ev3dev.core as core

def print_to_screen(string):
  string = str(string)

  screen = core.Screen()
  screen.clear()
  
  screen.draw.text((10,10), string, font=fonts.load('luBS24'))
  print(string)
  
  screen.update()

motor_a = ev3.LargeMotor('outA')
motor_a.reset()

print_to_screen(motor_a.position)

motor_a.run_to_rel_pos(position_sp=360, speed_sp=100, stop_action="brake")
motor_a.wait_while('running')

print_to_screen(motor_a.position)




