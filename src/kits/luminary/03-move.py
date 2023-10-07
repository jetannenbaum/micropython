from machine import Pin
from time import sleep
from neopixel import NeoPixel

NUMBER_PIXELS = 60
LED_PIN = 0

strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

while True:
    for i in range(0, NUMBER_PIXELS):
        strip[i] = (255,0,0) # red=255, green and blue are 0
        strip.write() # send the data from RAM down the wire
        sleep(.1) # keep on 1/10 of a second
        strip[i] = (0,0,0) # change the RAM back but don't resend the data
