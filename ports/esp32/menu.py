
import config
import wifi
import framebuf
from font import Font
import font2

  
class Menu:
  def __init__(self,ssd,json_file):
    self.ssd=ssd
    self.x1=10
    self.x2=44
    self.x3=77
    self.y=15
    self.path=json_file
  def disSensor(self,x,y,bat):
    alarm_on_off=config.get(self.path)['alarm']['on_off']
    #bat info
    ssd=self.ssd
    ssd.fill_rect(x,y,36,8,0)
    ssd.rect(x+20,y,16,8,1)
    w=round(bat*14)
    ssd.fill_rect(x+20+1,y+1,w,6,1)
    
    if wifi.sta.isconnected():
      fbuf = framebuf.FrameBuffer(bytearray(font2.wifi_8x8), 8, 8, framebuf.MONO_HLSB)
      ssd.blit(fbuf, x+10, 0)
    if alarm_on_off=='on':
      fbuf = framebuf.FrameBuffer(bytearray(font2.alarm_8x8), 8, 8, framebuf.MONO_HLSB)
      ssd.blit(fbuf, x, 0)   
    '''
    if bluetooth_on:
      fbuf = framebuf.FrameBuffer(bytearray(font2.bluetooth_8x8), 8, 8, framebuf.MONO_HLSB)
      ssd.blit(fbuf, x, 0)
    '''
    ssd.show()
  
  def clock(self): 
    ssd=self.ssd
    fbuf = framebuf.FrameBuffer(bytearray(Font.icon[0]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x1, self.y)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[0]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x2, self.y)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[1]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x3, self.y)
    ssd.show()

  
  def alarm(self):
    ssd=self.ssd
    fbuf = framebuf.FrameBuffer(bytearray(Font.icon[1]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x1, self.y)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[3]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x2, self.y)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[1]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x3, self.y)

    ssd.show()
  def compass(self):
    ssd=self.ssd
    fbuf = framebuf.FrameBuffer(bytearray(Font.icon[5]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x1, self.y)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[14]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x2, self.y)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[15]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x3, self.y)
   # fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[16]), 32, 32, framebuf.MONO_HLSB)
    #ssd.blit(fbuf, self.x3, self.y)

    ssd.show()
    
  def weather(self):
    ssd=self.ssd
    fbuf = framebuf.FrameBuffer(bytearray(Font.icon[3]), 32, 32, framebuf.MONO_HLSB)

    ssd.blit(fbuf, self.x1, self.y)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[4]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x2, self.y)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[5]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x3, self.y)
    ssd.show()
  def appstore(self):
    ssd=self.ssd
    fbuf = framebuf.FrameBuffer(bytearray(Font.icon[4]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x1, self.y)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[12]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x2, self.y)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[13]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x3, self.y)
    ssd.show()
    '''
  def codecase(self):
    fbuf = framebuf.FrameBuffer(bytearray(Font.icon[3]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, 10, 10)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[4]), 32, 32, framebuf.MONO_HLSB)

    ssd.blit(fbuf, 44, 10)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[5]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, 77, 10)
    ssd.show()
    '''
  def sysset(self):
    ssd=self.ssd

    fbuf = framebuf.FrameBuffer(bytearray(Font.icon[2]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x1, self.y)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[6]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x2, self.y)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[7]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, self.x3, self.y)
    ssd.show()
    
    
''' 
class Sysset:
  def __init__(self):
  
  def wifiset(self):
    
  def updatertc(self):
    
  def alarmset(self):

'''





















