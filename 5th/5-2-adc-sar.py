import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def to_list_of_bits(num):
    return [(num >> i) & 1 for i in range(num.bit_length() - 1, -1, -1)]
	
	
def clip_to_zero(num):
    return 0 if num < 0 else num
	
	
def extend_array(array, desired_size):
    return [0] * clip_to_zero(desired_size - len(array)) + array 
	
	
def extended_list_of_bits(num, desired_size = len(dac)):
    return extend_array(to_list_of_bits(num), desired_size)


def from_binary(bits):
    number = 0
    
    for bit in bits:
        number *= 2
        number += bit
    return number


def adc():
    size_in_bits = 8
    current_bits = [0] * size_in_bits  
     
    for i in range(size_in_bits):       
        current_bits[i] = 1
        GPIO.output(dac, current_bits)    
	    
        time.sleep(0.05)
        
        if GPIO.input(comp) == GPIO.LOW:
            current_bits[i] = 0  
	        
    return from_binary(current_bits)  


try:
    while True:
        bit_num = adc()
        voltage = bit_num * 3.3 / 256
        
        print(extended_list_of_bits(bit_num), "==", f"{bit_num:03}", " => ", f"{voltage:.3f} V")
        
except KeyboardInterrupt:
	print("Finished!")        
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
