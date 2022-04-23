import RPi.GPIO as GPIO
from time import sleep

if __name__ == "__main__":
    led_pins = [21, 20, 16, 12, 7, 8, 25, 24]
    aux_pins = [22, 23, 27, 18, 15, 14, 3, 2]

    assert (len (led_pins) == len (aux_pins))

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pins, GPIO.OUT)
    GPIO.setup(aux_pins, GPIO.IN)

    while True:
        for led_pin, aux_pin in zip (led_pins, aux_pins):
            GPIO.output (led_pin, GPIO.input(aux_pin))
                
    GPIO.cleanup()