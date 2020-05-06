"""
Team 2
Shower Scrubber
Main routine for the bot
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

# Step completed flags
map_done = False
wash_done = False
rinse_done = False

# LSW handling
lsw_one, lsw_two, lsw_seven, lsw_eight = False, False, False, False

def get_lsw_inputs():
    lsw_one = gpio.input(pins.LSW_ONE)
    lsw_two = gpio.input(pins.LSW_TWO)
    lsw_seven = gpio.input(pins.LSW_SEVEN)
    lsw_eight = gpio.input(pins.LSW_EIGHT)

def mapping_routine():
    """ Mapping routine for the bot, goes around the perimeter of the shower """
    num_turns = 0
    
    # Check initial LSW positions, if not placed correctly then abort
    get_lsw_inputs()
    if not (lsw_one and lsw_two and lsw_seven and lsw_eight):
        return
    
    # Initial turn 90° to the right
    movement.set_turn_right()
    
    while num_turns < 4:
        # Move forward until the LSWs are triggered
        movement.set_move_forward()
        get_lsw_inputs()

        # Move until a corner is hit
        while not (lsw_one and lsw_two and lsw_seven and lsw_eight):
            get_lsw_inputs()
        else:
            movement.set_move_stop()
        
        # Turn right
        movement.set_turn_right()
        num_turns += 1
    
    map_done = True

