"""
Team 2
Shower Scrubber
Main routine for the bot
"""

# Import statements
import pin_assignments as pins
import pin_setup
import RPi.gpio as gpio
import time

# Set up GPIO
pin_setup.set_io()
pin_setup.set_pwm()