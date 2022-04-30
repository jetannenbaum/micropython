from machine import Pin, Timer
import machine
import ssd1306
import time
import framebuf

WIDTH = 128
HEIGHT = 64
CS = machine.Pin(1)
DC = machine.Pin(4)
RES = machine.Pin(5)
clock=machine.Pin(2)
data=machine.Pin(3)
spi=machine.SPI(0,sck=clock, mosi=data)
oled = ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, DC, RES, CS)

# 64, 64, framebuf.MONO_VLSB
coderdojo_logo_byte_array = bytearray(
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00\x00\x00\x00\x04\x00\x00\x02\x00\x00\x80\xc1\xc1\xc0\xc0\xc0'
    b'\xc0\xc0\xc1\x81\x01\x01\x02\x02\x06\x0e\x0c\x1c\x38\xf8\xf8\xf0\xe0\xe0\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x40\x00\x00\x04\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\x00\x00\x00'
    b'\x00\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\xff\xff\xff\xff\xff\xff\xfe\xfc\xf8\xe0\xc0\x00\x00\x00\x00\x00'
    b'\x00\x80\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x1f\x38\x10\x10\x10'
    b'\x10\x30\x1f\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xf8\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xf8\xc0\x00'
    b'\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x80\x80\x80\xc0\xe0\xe0\xf0\xf8\xfc\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfc'
    b'\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xe0\xf0\xf8\xfc\xfc\xfe\xfe\xfe\xff\xff\xff\xff'
    b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x3f'
    b'\x00\x03\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf9\xf9\xf9\xf1'
    b'\x01\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x7f\x1f\x03\x00'
    b'\x00\x00\x00\x00\x00\x02\x00\x10\x20\x40\x80\x00\x00\x00\x00\x00\x0f\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x3f\x3f\x3f\x2f'
    b'\x00\x3f\x3f\x03\x03\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x7f\x3f\x1f\x0f\x03\x01\x00\x00\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x04\x00\x00\x10\x01\x23\x07\x0f\x5f\x3f\x3f\x7f\xff\xff\xff\xff\xff\xff'
    b'\xff\xff\xff\xff\xff\xff\x7f\x7f\x7f\x7f\x3f\x3f\x3f\x1f\x1f\x0f\x0f\x07\x03\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

fbi = framebuf.FrameBuffer(coderdojo_logo_byte_array, 64, 64, framebuf.MONO_VLSB)

while True:
    oled.fill(0)
    oled.blit(fbi, 64, 0)
    oled.text('CoderDojo', 0, 0)
    oled.text('Robots', 0, 10)
    oled.text('Standby', 0, 54)
    oled.show()