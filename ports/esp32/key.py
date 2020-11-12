
from machine import Pin,Timer

class Key:
  NONE_PRESS = const( 0 )
  HOME_PRESS = const( 1 )
  LEFT_PRESS = const( 2 )
  RIGHT_PRESS = const( 3 )
  BACK_PRESS = const( 4 )
  
  def __init__(self,home,left,right,back):      
    self.home = Pin(home,Pin.IN,Pin.PULL_UP)
    self.left = Pin(left,Pin.IN,Pin.PULL_UP)
    self.right = Pin(right,Pin.IN,Pin.PULL_UP)
    self.back = Pin(back,Pin.IN,Pin.PULL_UP)
    
    self.tim0=Timer(0)
    self.value=self.NONE_PRESS
    self.value_dic={
      14:self.HOME_PRESS,
      13:self.LEFT_PRESS,
      11:self.RIGHT_PRESS,
      7:self.BACK_PRESS,
      15:self.NONE_PRESS
    }
  def read(self):
    return self.value
  def getkey(self):
    data=(self.back.value()<<3)|((self.right.value()&0x0F)<<2)|((self.left.value()&0x0F)<<1)|(self.home.value())
    try:
      self.value=self.value_dic[data]
    except Exception:
      self.value=self.NONE_PRESS
    self.value
      
  
  def start(self):
    self.tim0.init(period=100,mode=Timer.PERIODIC,callback=lambda t:self.getkey())
  def stop(self):
    self.tim0.deinit()


