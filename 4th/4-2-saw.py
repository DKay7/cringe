import RPi.GPIO as GPIO
from time import sleep
from random import randint

#----------------------------------------------------------------------------------------------------

TOTAL_NUM_OF_BITS   = 8
MAX_VOLTAGE         = 3.3

#----------------------------------------------------------------------------------------------------

def num_to_byte_list (number):
    assert (number <= 255 and number >= 0)
    byte_list = [int(digit) for digit in bin(number)[2:]] # [2:] to chop off the "0b" part
    byte_list = [0] * (8 - len (byte_list)) + byte_list   # extend byte_list to len of 8
    return byte_list

#----------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    
    dac_pins = [26, 19, 13, 6, 5, 11, 9, 10]

    GPIO.setmode (GPIO.BCM)
    GPIO.setup (dac_pins, GPIO.OUT) 

    try:
        delay = float (input ("Введите период сигнала в секундах: "))
        while True:
            # incresing
            for cur_value in range(0, 2 ** TOTAL_NUM_OF_BITS - 1):
                bin_value = num_to_byte_list(cur_value)
                GPIO.output(dac_pins, bin_value)
                sleep (delay / 2 / 2 ** TOTAL_NUM_OF_BITS)
            
            # decresing
            for cur_value in range(2 ** TOTAL_NUM_OF_BITS - 1, 0 - 1, -1):
                bin_value = num_to_byte_list(cur_value)
                GPIO.output(dac_pins, bin_value)
                sleep (delay / 2 / 2 ** TOTAL_NUM_OF_BITS)
            
    except ValueError as e:
        print ('\u001b[31mВведенное вами число некорректно\u001b[0m')

    finally:
        GPIO.output (dac_pins, [0] * len(dac_pins))
        GPIO.cleanup()
    

