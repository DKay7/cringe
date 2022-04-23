import RPi.GPIO as GPIO
from time import sleep

def blink_all_leds (pins, delay=0.2):
    for pin in pins:
        GPIO.output (pin, GPIO.HIGH)
        sleep (delay)
        GPIO.output (pin, GPIO.LOW)

# -----------------------------------------------------

if __name__ == "__main__":
    led_pins = [21, 20, 16, 12, 7, 8, 25, 24]


    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pins, GPIO.OUT)

    for i in range (3):
        blink_all_leds (led_pins)
    
    GPIO.output (led_pins, GPIO.LOW)
    GPIO.cleanup()
    
