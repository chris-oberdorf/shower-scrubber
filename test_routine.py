"""
Team 2
Shower Scrubber
Testing routine for the bot
"""

# Import statements
import pin_assignments as pins
import pin_setup
import RPi.gpio as gpio
import helper_functions as movement
import time

# Set up GPIO
pin_setup.set_io()
pin_setup.set_pwm()

# Goal: Move forward spraying water until hitting a wall by limit switches, then shut off and turn
# Variable setup
finished = False
left_lsw, right_lsw = False, False

def get_lsw_inputs():
    left_lsw = gpio.input(pins.LSW_ONE)
    right_lsw = gpio.input(pins.LSW_TWO)

while not finished:
    if not gpio.input(pins.BTN_START):
        continue
    else:
        # Start brushes
        gpio.output(pins.BRUSH_ONE, True)
        gpio.output(pins.BRUSH_TWO, True)
        
        # Start water pump
        gpio.output(pins.SOL_WATER, True)
        time.sleep(1)
        gpio.output(pins.PUMP_WATER, True)
        
        # Add a short delay to make sure it works
        time.sleep(1)
        
        get_lsw_inputs()
        movement.set_move_forward()
        while not (left_lsw or right_lsw):
            get_lsw_inputs()
        else:
            set_move_stop()
        
        # Shut off brushes
        gpio.output(pins.BRUSH_ONE, False)
        gpio.output(pins.BRUSH_TWO, False)
        
        # Shut off other stuff
        gpio.output(pins.PUMP_WATER, False)
        time.sleep(1)
        gpio.output(pins.SOL_WATER, False)
        
        # Turn left
        movement.set_turn_left()