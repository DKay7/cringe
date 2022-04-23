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

def count_voltage_by_number (num):
    assert 0 <= num <= 2 ** TOTAL_NUM_OF_BITS - 1

    approx_voltage = num * (MAX_VOLTAGE / 2 ** TOTAL_NUM_OF_BITS)

    return approx_voltage

#----------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    

    dac_pins = [26, 19, 13, 6, 5, 11, 9, 10]

    GPIO.setmode (GPIO.BCM)
    GPIO.setup (dac_pins, GPIO.OUT) 

    try:
        user_input = input("\u001b[32mВведите число от 0 до 255 или 'q' для выхода:\u001b[0m ")

        if user_input == 'q':
            exit(0)
        
        user_num = int(user_input)
        assert 0 <= user_num <= 2 ** TOTAL_NUM_OF_BITS - 1

        user_bin_num = num_to_byte_list(user_num)
        GPIO.output(dac_pins, user_bin_num)
        print (f"\u001b[32mРасчетное напряжение на выходе DAC: \u001b[0m~{count_voltage_by_number(user_num)} В.")
        
        sleep (15)

    except AssertionError as e:
        print ('\u001b[31mВведенное вами число некорректно\u001b[0m')

    except ValueError:
        print ("\u001b[31mНужно ввести целое число или 'q' для выхода\u001b[0m")

    finally:
        GPIO.output (dac_pins, [0] * len(dac_pins))
        GPIO.cleanup()
    
