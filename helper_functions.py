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

# Set up pins and set motors as well as turn delay
pin_setup.set_io()
pin_setup.set_pwm()

LEFT_WHEEL = pin_setup.MOTOR_LEFT
RIGHT_WHEEL = pin_setup.MOTOR_RIGHT
TURN_DELAY = 5 # in seconds

def set_move_forward():
    # Set left wheel clockwise, right wheel counterclockwise
    gpio.output(pins.LEFT_CW, True)
    gpio.output(pins.LEFT_CCW, False)
    gpio.output(pins.RIGHT_CW, False)
    gpio.output(pins.RIGHT_CCW, True)
    
    # Set both motors running at 100% duty cycle
    LEFT_WHEEL.ChangeDutyCycle(100)
    RIGHT_WHEEL.ChangeDutyCycle(100)

def set_move_reverse():
    # Set left wheel counterclockwise, right wheel clockwise
    gpio.output(pins.LEFT_CW, False)
    gpio.output(pins.LEFT_CCW, True)
    gpio.output(pins.RIGHT_CW, True)
    gpio.output(pins.RIGHT_CCW, False)
    
    # Set both motors running at 100% duty cycle
    LEFT_WHEEL.ChangeDutyCycle(100)
    RIGHT_WHEEL.ChangeDutyCycle(100)
    
def set_move_stop():
    # Set left wheel and right wheel to no direction
    gpio.output(pins.LEFT_CW, False)
    gpio.output(pins.LEFT_CCW, False)
    gpio.output(pins.RIGHT_CW, False)
    gpio.output(pins.RIGHT_CCW, False)
    
    # Set both motors to 0% duty cycle
    LEFT_WHEEL.ChangeDutyCycle(0)
    RIGHT_WHEEL.ChangeDutyCycle(0)

def set_turn_left():
    # Set left wheel and right wheel to clockwise
    gpio.output(pins.LEFT_CW, True)
    gpio.output(pins.LEFT_CCW, False)
    gpio.output(pins.RIGHT_CW, True)
    gpio.output(pins.RIGHT_CCW, False)
    
    # Set both motors to 50% duty cycle
    LEFT_WHEEL.ChangeDutyCycle(50)
    RIGHT_WHEEL.ChangeDutyCycle(50)
    
    # Delay then turn off wheels
    time.sleep(TURN_DELAY)
    set_move_stop()

def set_turn_right():
    # Set left wheel and right wheel to counterclockwise
    gpio.output(pins.LEFT_CW, False)
    gpio.output(pins.LEFT_CCW, True)
    gpio.output(pins.RIGHT_CW, False)
    gpio.output(pins.RIGHT_CCW, True)
    
    # Set both motors to 50% duty cycle
    LEFT_WHEEL.ChangeDutyCycle(50)
    RIGHT_WHEEL.ChangeDutyCycle(50)
    
    # Delay then turn off wheels
    time.sleep(TURN_DELAY)
    set_move_stop()