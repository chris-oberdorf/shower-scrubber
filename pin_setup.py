"""
Team 2
Shower Scrubber
File containing the setup functions for all GPIO pins
to assist in cleanliness of the main file.

Contains:
- set_io [Sets up all pins as the right IO]
- set_pwm [Sets up the wheel PWM]
"""

# Import statements
import pin_assignments as pins
import RPi.GPIO as gpio

# PWM frequency, in Hz
FREQ = 100

def set_io():
    # Start GPIO setup
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM) # Use GPIO numbering
    
    # Start button: Input
    gpio.setup(pins.BTN_START, gpio.IN)
    
    # Pumps: Output
    gpio.setup(pins.PUMP_WATER, gpio.OUT)
    gpio.setup(pins.PUMP_SOAP, gpio.OUT)
    
    # Solenoids: Output
    gpio.setup(pins.SOL_WATER, gpio.OUT)
    gpio.setup(pins.SOL_SOAP, gpio.OUT)
    
    # Limit switches: Input
    gpio.setup(pins.LSW_ONE, gpio.IN)
    gpio.setup(pins.LSW_TWO, gpio.IN)
    gpio.setup(pins.LSW_THREE, gpio.IN)
    gpio.setup(pins.LSW_FOUR, gpio.IN)
    gpio.setup(pins.LSW_FIVE, gpio.IN)
    gpio.setup(pins.LSW_SIX, gpio.IN)
    gpio.setup(pins.LSW_SEVEN, gpio.IN)
    gpio.setup(pins.LSW_EIGHT, gpio.IN)
    
    # Brush motors: Output
    gpio.setup(pins.BRUSH_ONE, gpio.OUT)
    gpio.setup(pins.BRUSH_TWO, gpio.OUT)
    
    # Wheel 1: PWM and output
    gpio.setup(pins.LEFT_PWM, gpio.OUT)
    gpio.setup(pins.LEFT_CW, gpio.OUT)
    gpio.setup(pins.LEFT_CCW, gpio.OUT)
    
    # Wheel 2: PWM and output
    gpio.setup(pins.RIGHT_PWM, gpio.OUT)
    gpio.setup(pins.RIGHT_CW, gpio.OUT)
    gpio.setup(pins.RIGHT_CCW, gpio.OUT)
    
    # Left encoder: Input
    gpio.setup(pins.LEFT_ENC_A, gpio.IN)
    gpio.setup(pins.LEFT_ENC_B, gpio.IN)
    
    # Right encoder: Input
    gpio.setup(pins.RIGHT_ENC_A, gpio.IN)
    gpio.setup(pins.RIGHT_ENC_B, gpio.IN)
    
    # Water level sensor: Input
    gpio.setup(pins.LEVEL_SENSOR, gpio.IN)
    
def set_pwm():
    MOTOR_LEFT = gpio.PWM(pins.LEFT_PWM, FREQ)
    MOTOR_LEFT.start(0) # Initialize with 0% D.C.
    
    MOTOR_RIGHT = gpio.PWM(pins.RIGHT_PWM, FREQ)
    MOTOR_RIGHT.start(0) # Initialize with 0% D.C.