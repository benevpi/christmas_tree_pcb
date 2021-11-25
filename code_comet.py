# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example displays the basic animations in sequence, at a five second interval.

For NeoPixel FeatherWing. Update pixel_pin and pixel_num to match your wiring if using
a different form of NeoPixels.

This example may not work on SAMD21 (M0) boards.
"""
import board
import neopixel
import pwmio

from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import (
    RED,
    GREEN,
    PURPLE,
    WHITE,
    AMBER,
    JADE,
    TEAL,
    PINK,
    MAGENTA,
    ORANGE,
)

leds_1pin = pwmio.PWMOut(board.GP4, frequency=5000, duty_cycle=0)
leds_2pin = pwmio.PWMOut(board.GP5, frequency=5000, duty_cycle=0)

leds_1_value = 0
leds_2_value = 65000

leds_1_direction = 1
leds_2_direction = -1

leds_step = 50

# Update to match the pin connected to your NeoPixels
pixel_pin = board.GP28
# Update to match the number of NeoPixels you have connected
pixel_num = 7

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.5, auto_write=False)

comet_1 = Comet(pixels, speed=0.1, color=PURPLE, tail_length=3, bounce=False)
comet_2 = Comet(pixels, speed=0.1, color=RED, tail_length=3, bounce=False, reverse=True)
comet_3 = Comet(pixels, speed=0.1, color=TEAL, tail_length=3, bounce=False)
comet_4 = Comet(pixels, speed=0.1, color=GREEN, tail_length=3, bounce=False, reverse=True)

animations = AnimationSequence(
    comet_1,
    comet_2, comet_3, comet_4, advance_interval=1.1, auto_reset=True,
)

while True:
    animations.animate()
    
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
