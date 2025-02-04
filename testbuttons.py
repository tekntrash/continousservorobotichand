import Jetson.GPIO as GPIO
import time

# Pin Definitions
button_pinin = 16  # GPIO pin for button IN 
button_pinout = 18  # GPIO pin for button OUT

# Setup GPIO
GPIO.setmode(GPIO.BOARD)  # Use BOARD pin numbering
GPIO.setup(button_pinin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set pin as input with pull-up resistor
GPIO.setup(button_pinout, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set pin as input with pull-up resistor

try:
    print("Waiting for button press...")
    while True:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
        # Read the button state
        button_statein = GPIO.input(button_pinin)
        button_stateout = GPIO.input(button_pinout)
        
        # Check if the button is pressed (LOW state)
        if button_statein == GPIO.HIGH:
            # Get the current time
            print(f"Button IN pressed at {current_time}!")
        
        if button_stateout == GPIO.HIGH:
            # Get the current time
            print(f"Button OUT pressed at {current_time}!")
        
        # Small delay to avoid high CPU usage
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Clean up GPIO on exit
    GPIO.cleanup()
