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

def count_voltage_by_duty (duty):
    assert 0 <= duty <= 100

    approx_voltage = MAX_VOLTAGE * duty / 100

    return approx_voltage

#----------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    
    pwm_pin = 18

    frequency = 1000
    duty_cycle = 0

    GPIO.setmode (GPIO.BCM)
    GPIO.setup (pwm_pin, GPIO.OUT) 
    
    pwm_output = GPIO.PWM(pwm_pin, frequency)
    pwm_output.start(0)

    try:
        while True:
            duty_cycle = int (input ("Введите D: "))
            pwm_output.ChangeDutyCycle(duty_cycle)

            print (f"\u001b[32mРасчетное напряжение на выходе: \u001b[0m~{count_voltage_by_duty(duty_cycle)} В.")

    except ValueError as e:
        print ('\u001b[31mВведенное вами число некорректно\u001b[0m')

    finally:
        pwm_output.stop()
        GPIO.output (pwm_pin, 0)
        GPIO.cleanup()
    

