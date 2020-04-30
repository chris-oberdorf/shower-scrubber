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
