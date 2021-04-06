## SSD1306 OLED Display example
**Send messages and sensor date to an I2C driven ssd1306 OLED display** <br />

**You must upload the _ssd1306.py_ module to the board in order to use the included code examples**<br />

The _ssd1306.py_ module was written by Alex Newton and published at the following link: [how2electronics-ssd1306](https://how2electronics.com/interfacing-ssd1306-oled-display-with-raspberry-pi-pico/) <br />

### To test if we have a functional connection with the display (or any i2c device), the following lines will do the trick

```python
from machine import Pin, I2C
# assuming we are connected to I2C port 0 on GPIO pins 8 and 9 of the Raspberry Pico
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000) 
i2c.scan()
```

### oledHello.py

This is a very minimal code to show simple text on the screen

### oledSensorData.py

This is the final code example. It is suggested to use a potentiometer to test. Any analog sensor may be used instead 

### Hookup guide:

![schematic](ssd1306-pot.png)

