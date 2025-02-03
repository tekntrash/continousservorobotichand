import random
import Jetson.GPIO as GPIO
from adafruit_servokit import ServoKit
import time
import sys

# Pin Definitions
button_pinin = 16   # GPIO pin for "IN" button
button_pinout = 18  # GPIO pin for "OUT" button

# Setup GPIO
GPIO.cleanup()  
GPIO.setmode(GPIO.BOARD)  # Use BOARD pin numbering
GPIO.setup(button_pinin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set pin as input with pull-up resistor
GPIO.setup(button_pinout, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set pin as input with pull-up resistor

# Initialize the ServoKit instance for PCA9685 (16 channels supported)
kit = ServoKit(channels=16)

# Define the servo channel and default state
servo_channel = 4
angle = 130  # Initial angle
direction = "IN"
moveservo=1

# Log file to store runtime information
log_file = "servo5.txt"


#108 to 180
#1 to 90 
# Initialize the start time
start_time = time.perf_counter()
try:
    while True:
        button_statein = GPIO.input(button_pinin)
        if GPIO.input(button_pinin) == GPIO.HIGH:  # Button pressed
            print ("Button IN pressed!")
            direction = "IN"
            angle = random.randint(1, 90)
            moveservo=1

        button_stateout = GPIO.input(button_pinout)
        if GPIO.input(button_pinout) == GPIO.HIGH:  # Button pressed
            print ("Button OUT pressed!")
            direction = "OUT"
            angle = random.randint(108,180)
            moveservo=1

        if moveservo==1:
          moveservo=0
          kit.servo[servo_channel].angle = angle  
          end_time = time.perf_counter()
          total_runtime = end_time - start_time
          log_message = f"{direction}, {total_runtime:.9f}, {angle}, {servo_channel}\n"
          print(log_message.strip())
          with open(log_file, "a") as file:
            file.write(log_message)
          start_time = time.perf_counter()

        time.sleep(0.01)  # Poll every 10ms
except KeyboardInterrupt:
    kit.servo[servo_channel].angle = 91  # Stop position
    print("Exiting...")
finally:
    GPIO.cleanup()  # Clean up GPIO on exit
