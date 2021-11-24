import time
import pwmio
import board
import neopixel
import digitalio

try:
    import urandom as random
except ImportError:
    import random
'''    
leds_1 = pwmio.PWMOut(board.GP4, frequency=5000, duty_cycle=0)
leds_2 = pwmio.PWMOut(board.GP5, frequency=5000, duty_cycle=0)

'''
j=0
led_1 = led = digitalio.DigitalInOut(board.GP4)
led_2 = led = digitalio.DigitalInOut(board.GP5)

led_1.direction = digitalio.Direction.OUTPUT
led_2.direction = digitalio.Direction.OUTPUT
    
bright_div = 20
numpix = 7  # Number of NeoPixels
pixpin = board.GP28
# Pin where NeoPixels are connected
strip = neopixel.NeoPixel(pixpin, numpix, brightness=1, auto_write=False)
colors = [
    [232, 50, 50], 
    [200, 200, 20], 
    [30, 200, 200], 
    [30, 20, 200],
    [30, 200, 20],  
]

max_len=20
min_len = 8
#pixelnum, posn in flash, flash_len, direction
flashing = []

num_flashes = 3

for i in range(num_flashes):
    pix = random.randint(0, numpix - 1)
    col = random.randint(1, len(colors) - 1)
    flash_len = random.randint(min_len, max_len)
    flashing.append([pix, colors[col], flash_len, 0, 1])
    
strip.fill((0,0,0))

while True:
    strip.show()
    for i in range(num_flashes):
        pix = flashing[i][0]
        brightness = (flashing[i][3]/flashing[i][2])
        colr = (int(flashing[i][1][0]*brightness), 
                int(flashing[i][1][1]*brightness), 
                int(flashing[i][1][2]*brightness))
        strip[pix] = colr
        if flashing[i][2] == flashing[i][3]:
            flashing[i][4] = -1
        if flashing[i][3] == 0 and flashing[i][4] == -1:
            pix = random.randint(0, numpix - 1)
            col = random.randint(0, len(colors) - 1)
            flash_len = random.randint(min_len, max_len)
            flashing[i] = [pix, colors[col], flash_len, 0, 1]
        flashing[i][3] = flashing[i][3] + flashing[i][4]
        # PWM LED up and down
    if j < 50:
        led_1.value = True
        led_2.value = False
    else:
        led_1.value = False
        led_2.value = True
    j = j+1
    if(j>100): j=0
    time.sleep(0.01)
