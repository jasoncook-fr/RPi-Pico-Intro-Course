# Display sensor data on I2C driven ssd1306 OLED display 
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C

sensor = ADC(26) # ADC0 on Raspberry Pico

WIDTH  = 128 # oled display width
HEIGHT = 64  # oled display height

# Init I2C using pins GP8 & GP9 (default I2C0 pins)
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)

# Init oled display
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

while True:
    reading = sensor.read_u16()
 
    # Clear the oled display
    oled.fill(0)
       
    # add text
    oled.text("ADC: ",5,8)
    # add sensor data
    oled.text(str(round(reading,2)),40,8)
 
    # update the oled display to show our message
    oled.show()