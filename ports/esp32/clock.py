





import framebuf
from machine import RTC,Pin,ADC
import time
from font import Font
from sht30 import SHT30
import wifi
import beep

def getBatV():
  adc = ADC(Pin(34))          # create ADC object on ADC pin
  #adc.read()                  # read value, 0-4095 across voltage range 0.0v - 1.0v

  adc.atten(ADC.ATTN_11DB)    # set 11dB input attentuation (voltage range roughly 0.0v - 3.6v)
  adc.width(ADC.WIDTH_9BIT)   # set 9 bit return values (returned range 0-511)
  return round(adc.read()/512*3.6*2,2)
 
def getTemp():
  sensor = SHT30() 
  return sensor.measure()
    
class Clock:
  def __init__(self,ssd,key):
    self.ssd=ssd
    self.key=key
    self.rtc=RTC()
    self.week_dic={0:'SU',1:'MO',2:'TU',3:'WE',4:'TH',5:'FR',6:'SA'}
    self.mode=0 #0:clock; 1:timer
    
    self.tr_cnt=0
    self.tr_set_hour=0
    self.tr_set_min=0
    self.tr_set_sec=0
    self.tr_hour=0
    self.tr_min=0
    self.tr_sec=0
    self.tr_on_off=False
    self.tr_set_p=0
    self.tr_beep_cnt=30
    self.tr_beep_start=False
  def run(self):
    while True:
      keyvalue= self.key.read()
      
      dt=self.rtc.datetime()
        
      year=dt[0]
      mon=dt[1]
      day=dt[2]
      week=dt[3]
      
      hour=dt[4]
      min=dt[5]
      sec=dt[6]
        
      if self.mode==0: 

        
        self.ssd.fill_rect(90,5,127,13,0)  
        self.ssd.fill_rect(10,50,127,58,0)   
        date=str(year)+'-'+str(mon)+'-'+str(day)
        self.ssd.text(date,0,5)
        

        #self.ssd.text('%.2f' % getBatV(),90,5)
        self.ssd.text(self.week_dic[week],90,5)
        temperature, humidity = getTemp()
        self.ssd.text('%.2f' % temperature+' '+'%.2f' % humidity,10,50)
        
        
        fbuf = framebuf.FrameBuffer(bytearray(Font.nums[hour//10]), 16, 33, framebuf.MONO_HLSB)
        self.ssd.blit(fbuf, 0, 15)
        fbuf = framebuf.FrameBuffer(bytearray(Font.nums[hour%10]), 16, 33, framebuf.MONO_HLSB)
        self.ssd.blit(fbuf, 17, 15)
        fbuf = framebuf.FrameBuffer(bytearray(Font.maohao), 16, 33, framebuf.MONO_HLSB)
        self.ssd.blit(fbuf, 34, 15)
        
        fbuf = framebuf.FrameBuffer(bytearray(Font.nums[min//10]), 16, 33, framebuf.MONO_HLSB)
        self.ssd.blit(fbuf, 51, 15)
        fbuf = framebuf.FrameBuffer(bytearray(Font.nums[min%10]), 16, 33, framebuf.MONO_HLSB)
        self.ssd.blit(fbuf, 68, 15)
        fbuf = framebuf.FrameBuffer(bytearray(Font.nums_small[sec//10]), 10, 20, framebuf.MONO_HLSB)
        self.ssd.blit(fbuf, 90, 25)
        fbuf = framebuf.FrameBuffer(bytearray(Font.nums_small[sec%10]), 10, 20, framebuf.MONO_HLSB)
        self.ssd.blit(fbuf, 101, 25)
        self.ssd.show()
        
      elif self.mode==1:
        self.ssd.text('TR',0,5)
        
        
        self.ssd.fill_rect(20,4,64,10,1)
        self.ssd.text('%02d' % self.tr_set_hour+':'+'%02d' % self.tr_set_min+':'+'%02d' % self.tr_set_sec,20,5,0)
        
        #self.ssd.rect(80,3,42,11,1)
        if self.tr_on_off:
          self.ssd.text('START',87,5,1)
        else:
          self.ssd.text('STOP',87,5,1)
        
        fbuf = framebuf.FrameBuffer(bytearray(Font.nums[self.tr_hour//10]), 16, 33, framebuf.MONO_HLSB)
        self.ssd.blit(fbuf, 0, 15)
        fbuf = framebuf.FrameBuffer(bytearray(Font.nums[self.tr_hour%10]), 16, 33, framebuf.MONO_HLSB)
        self.ssd.blit(fbuf, 17, 15)
        fbuf = framebuf.FrameBuffer(bytearray(Font.maohao), 16, 33, framebuf.MONO_HLSB)
        self.ssd.blit(fbuf, 34, 15)
        
        fbuf = framebuf.FrameBuffer(bytearray(Font.nums[self.tr_min//10]), 16, 33, framebuf.MONO_HLSB)
        self.ssd.blit(fbuf, 51, 15)
        fbuf = framebuf.FrameBuffer(bytearray(Font.nums[self.tr_min%10]), 16, 33, framebuf.MONO_HLSB)
        self.ssd.blit(fbuf, 68, 15)
        fbuf = framebuf.FrameBuffer(bytearray(Font.nums_small[self.tr_sec//10]), 10, 20, framebuf.MONO_HLSB)
        self.ssd.blit(fbuf, 90, 25)
        fbuf = framebuf.FrameBuffer(bytearray(Font.nums_small[self.tr_sec%10]), 10, 20, framebuf.MONO_HLSB)
        self.ssd.blit(fbuf, 101, 25)
        
        if self.tr_set_p==1:
          self.ssd.rect(0,14,34,34,1)
        elif self.tr_set_p==2:
          self.ssd.rect(51,14,34,34,1)
        elif self.tr_set_p==3:
          self.ssd.rect(90,24,21,21,1)
        elif self.tr_set_p==4:
          self.ssd.rect(87,3,41,11,1)
        
        self.ssd.show()
        
        
        if keyvalue==self.key.LEFT_PRESS:
          self.ssd.rect(0,14,34,34,0)

          self.ssd.rect(51,14,34,34,0)
          self.ssd.rect(90,24,21,21,0)
          self.ssd.rect(87,3,41,11,0)
          self.tr_set_p+=1
          if self.tr_set_p>=5:
            self.tr_set_p=0
          time.sleep_ms(200)
        if keyvalue==self.key.RIGHT_PRESS:

          self.ssd.fill_rect(87,5,42,8,0)
          if self.tr_set_p==1:
            self.tr_hour+=1
            if self.tr_hour>=24:
              self.tr_hour=0
          elif self.tr_set_p==2:
            self.tr_min+=1
            if self.tr_min>=60:
              self.tr_min=0
          elif self.tr_set_p==3:
            self.tr_sec+=1
            if self.tr_sec>=60:
              self.tr_sec=0
          elif self.tr_set_p==4:
            if self.tr_on_off:
              self.tr_on_off=False
            else:
              self.tr_on_off=True 
          if self.tr_on_off:  
            self.tr_set_hour= self.tr_hour
            self.tr_set_min= self.tr_min
            self.tr_set_sec= self.tr_sec
          time.sleep_ms(200)  
          
        
        if self.tr_on_off:
          if abs(self.tr_cnt-sec)>=1:
            self.tr_cnt=sec
            self.tr_sec-=1
            if self.tr_sec<0:
              if self.tr_min>0:
                self.tr_sec=59
                self.tr_min-=1
              elif self.tr_hour>0:
                self.tr_sec=59
                self.tr_min=59
                self.tr_hour-=1
              else:  #time is up
                self.ssd.fill_rect(87,5,41,8,0)
                self.tr_sec=0
                self.tr_on_off=False
                self.tr_beep_start=True        
        if self.tr_beep_start and self.tr_beep_cnt>0:
          self.tr_beep_cnt-=1
          if self.tr_beep_cnt<=0:
            self.tr_beep_cnt=30
            self.tr_beep_start=False
          beep.didi()
             
      if keyvalue==self.key.HOME_PRESS:
        if self.mode==0:
          self.mode=1
        elif self.mode==1:
          self.mode=0
        self.ssd.fill(0)
        time.sleep_ms(200)
      if keyvalue==self.key.BACK_PRESS:
        break
 









