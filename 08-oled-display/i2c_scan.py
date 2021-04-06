#Simple I2C code to check and see if we find a connected I2C device address

from machine import Pin, I2C

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000) 
i2c.scan()
