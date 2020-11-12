

from ssd1306 import SSD1306_SPI
from ssd1306 import SSD1306
from machine import Pin, SPI

WIDTH = const(128)
HEIGHT = const (64)

class Oled:
  def __init__(self,pin_dc,pin_cs,pin_rst,pin_sck,pin_mosi,pin_miso):
    pdc = Pin(pin_dc, Pin.OUT)   #27
    pcs = Pin(pin_cs, Pin.OUT)   #26
    prst = Pin(pin_rst, Pin.OUT)  #18
    #sck:22;   mosi:23;   miso:4
    #spi = SPI(baudrate=100000, polarity=1, phase=0, sck=Pin(pin_sck), mosi=Pin(pin_mosi), miso=Pin(pin_miso))
    spi = SPI(1, 80000000, sck=Pin(14), mosi=Pin(13))
    #spi.init(baudrate=200000) # set the baudrate
    self.ssd = SSD1306_SPI(WIDTH, HEIGHT, spi, pdc, prst, pcs)







