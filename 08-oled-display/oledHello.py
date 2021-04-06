# Simple message using an ssd1306 oled display 
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
 
WIDTH  = 128 # oled display width
HEIGHT = 64  # oled display height
 
# Init I2C using pins GP8 & GP9 (default I2C0 pins)
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)

# Init oled display
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Clear the oled display in case it has junk on it
oled.fill(0)

# Add some text
oled.text("ESAM <3 DOME",15,15)

oled.text("4-EVER",40,40)

# update the oled display to show our message
oled.show()