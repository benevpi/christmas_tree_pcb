import time
import board
from rainbowio import colorwheel
import neopixel
import pwmio

pixel_pin = board.GP28
num_pixels = 7

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

leds_1pin = pwmio.PWMOut(board.GP4, frequency=5000, duty_cycle=0)
leds_2pin = pwmio.PWMOut(board.GP5, frequency=5000, duty_cycle=0)

leds_1_value = 0
leds_2_value = 65000

leds_1_direction = 1
leds_2_direction = -1

leds_step = 500

def rainbow_cycle(wait):
    global leds_1_value
    global leds_2_value
    global leds_1_direction
    global leds_2_direction
    global leds_step
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        
        leds_1pin.duty_cycle = leds_1_value
        leds_2pin.duty_cycle = leds_2_value
        
        leds_1_value = leds_1_value + (leds_1_direction * leds_step)
        leds_2_value = leds_2_value + (leds_2_direction * leds_step)
        
        if (leds_1_value > 65000):
            leds_1_value = 65000
            leds_1_direction = -1
        if (leds_1_value < 0):
            leds_1_value = 0
            leds_1_direction = 1
            
        if (leds_2_value > 65000):
            leds_2_value = 65000
            leds_2_direction = -1
        if (leds_2_value < 0):
            leds_2_value = 0
            leds_2_direction = 1
        
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while True:


    #color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    #color_chase(YELLOW, 0.1)
    #color_chase(GREEN, 0.1)
    #color_chase(CYAN, 0.1)
    #color_chase(BLUE, 0.1)
    #color_chase(PURPLE, 0.1)

    rainbow_cycle(0.01)  # Increase the number to slow down the rainbow
