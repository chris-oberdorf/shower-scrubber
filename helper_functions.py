"""
Team 2
Shower Scrubber
Helper functions for bot code

Contains:
- set_move_forward : Sets both wheels to forward
- set_move_reverse : Sets both wheels to reverse
- set_move_stop    : Stops both wheels
- set_turn_left    : Turns the bot 90 degrees left
- set_turn_right   : Turns the bot 90 degrees right
"""

# Import statements
import pin_assignments as pins
import pin_setup
import RPi.gpio as gpio
import time

# Set up pins and set motors
pin_setup.set_io()
pin_setup.set_pwm()

LEFT_WHEEL = pin_setup.MOTOR_LEFT
RIGHT_WHEEL = pin_setup.MOTOR_RIGHT

def set_move_forward():
    # Set left wheel clockwise, right wheel counterclockwise
    gpio.output(pins.LEFT_CW, True)
    gpio.output(pins.LEFT_CCW, False)
    gpio.output(pins.RIGHT_CW, False)
    gpio.output(pins.RIGHT_CCW, True)
    
    # Set both motors running at 100% duty cycle
    LEFT_WHEEL.ChangeDutyCycle(100)
    RIGHT_WHEEL.ChangeDutyCycle(100)

