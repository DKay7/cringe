import RPi.GPIO as GPIO
import time

if __name__ == "__main__":
    out_pin = 17
    in_pin = 27

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(out_pin, GPIO.OUT)
    GPIO.setup(in_pin, GPIO.IN)

    while True:
        GPIO.output(out_pin, GPIO.input(in_pin))
