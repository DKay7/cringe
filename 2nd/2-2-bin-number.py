import RPi.GPIO as GPIO
from time import sleep
from random import randint

def num_to_byte_list (number):
    assert (number <= 255 and number >= 0)
    byte_list = [int(digit) for digit in bin(number)[2:]] # [2:] to chop off the "0b" part
    byte_list = [0] * (8 - len (byte_list)) + byte_list   # extend byte_list to len of 8
    return byte_list


if __name__ == "__main__":
    dac_pins = [26, 19, 13, 6, 5, 11, 9, 10]
    GPIO.cleanup()
    
    # generates 0 and 1 random sequense same len as DAC
    # bits_digits  = [randint (0, 1) for _ in dac_pins]

    # write given in binary to bits-digits
    bits_digits = num_to_byte_list (96)
    assert (len(dac_pins) == len(bits_digits))

    print (f" bits: {bits_digits}\n")

    GPIO.setmode (GPIO.BCM)
    GPIO.setup (dac_pins, GPIO.OUT) 

    GPIO.output (dac_pins, bits_digits) 
    sleep (15)



    GPIO.output (dac_pins, GPIO.LOW)
    GPIO.cleanup()
