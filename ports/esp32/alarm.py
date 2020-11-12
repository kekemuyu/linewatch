



import time
import framebuf
from machine import RTC
from font import Font
import config
from beep import Beep

def disdate(ssd,year,mon,day,hour,min,sec,on_off):
  ssd.fill_rect(0,5,127,8,0)
  date=str(year)+'-'+('%02d' % mon)+'-'+('%02d' % day)
  ssd.text(date,0,5)
  
  ssd.text(on_off,101,5)
  
  fbuf = framebuf.FrameBuffer(bytearray(Font.nums[hour//10]), 16, 33, framebuf.MONO_HLSB)
  ssd.blit(fbuf, 0, 15)
  fbuf = framebuf.FrameBuffer(bytearray(Font.nums[hour%10]), 16, 33, framebuf.MONO_HLSB)
  ssd.blit(fbuf, 17, 15)
  fbuf = framebuf.FrameBuffer(bytearray(Font.maohao), 16, 33, framebuf.MONO_HLSB)
  ssd.blit(fbuf, 34, 15)
  
  fbuf = framebuf.FrameBuffer(bytearray(Font.nums[min//10]), 16, 33, framebuf.MONO_HLSB)
  ssd.blit(fbuf, 51, 15)
  fbuf = framebuf.FrameBuffer(bytearray(Font.nums[min%10]), 16, 33, framebuf.MONO_HLSB)
  ssd.blit(fbuf, 68, 15)
  fbuf = framebuf.FrameBuffer(bytearray(Font.nums_small[sec//10]), 10, 20, framebuf.MONO_HLSB)
  ssd.blit(fbuf, 90, 25)
  fbuf = framebuf.FrameBuffer(bytearray(Font.nums_small[sec%10]), 10, 20, framebuf.MONO_HLSB)
  ssd.blit(fbuf, 101, 25)
  ssd.show()
 
def flash_rect(ssd,x,y,w,h,on_off):
  if w==0 and h==0:
    return
  if on_off:
    ssd.rect(x,y,w,h,1)
  else:
    ssd.rect(x,y,w,h,0)
  ssd.show()

class Alarm:
  def __init__(self,ssd,key,json_path):
    self.ssd=ssd
    self.key=key
    self.year=0
    self.mon=0
    self.day=0
    self.hour=0
    self.min=0
    self.sec=0
    self.path=json_path
    self.duty=100
    self.rect_flash_on_off=False
    b=Beep(key,60,json_path)
    b.start()
  def run(self):
    ssd=self.ssd
    key=self.key
    
  
    dt=config.get(self.path)['alarm']
    
    year=dt['year']
    mon=dt['mon']
    day=dt['day']
    
    hour=dt['hour']

    min=dt['min']
    sec=dt['sec']
        
    on_off=dt['on_off']
    
    disdate(ssd,year,mon,day,hour,min,sec,on_off)
    select_index=1
    
    select_x=0
    select_y=0
    select_w=0
    select_h=0
    
    while True:
      keyvalue=key.read()
      
      if select_index==1:
        select_x=0
        select_y=3
        select_w=32
        select_h=12
      elif select_index==2:
        select_x=40
        select_y=3
        select_w=16
        select_h=12
      elif select_index==3:
        select_x=64
        select_y=3
        select_w=16
        select_h=12
    
      elif select_index==4:
        select_x=0
        select_y=15
        select_w=32
        select_h=33
    
      elif select_index==5:
        select_x=51
        select_y=15
        select_w=32
        select_h=33


      elif select_index==6:
        select_x=90
        select_y=25
        select_w=20
        select_h=20
      elif select_index==7:   #on-off
        select_x=100 
        select_y=3
        select_w=24 
        select_h=12
   
      self.duty-=1
      if self.duty<=0:
        self.duty=100
        self.rect_flash_on_off=not self.rect_flash_on_off
      
      flash_rect(ssd,select_x,select_y,select_w,select_h,self.rect_flash_on_off)
    
      if keyvalue==key.LEFT_PRESS:

        if select_index==1:


          year-=1
        elif select_index==2:
      
          mon-=1
          if mon<1:
            mon=1
        elif select_index==3:
    
          day-=1
          if day<1:
            day=1
        elif select_index==4:
        
          hour-=1
          if hour<0:
            hour=0
        elif select_index==5:
        
          min-=1
          if min<0:
            min=1

        elif select_index==6:
         
          sec-=1
          if sec<0:
            sec=0
        elif select_index==7:
        
          if on_off=='off':
            on_off='on'
          else:
            on_off='off'
        disdate(ssd,year,mon,day,hour,min,sec,on_off)
        time.sleep_ms(200)
      elif keyvalue ==key.RIGHT_PRESS:
        if select_index==1:
       
          year+=1
        elif select_index==2:
      
          mon+=1
          if mon>12:
            mon=12
        elif select_index==3:
       
          day+=1
          if day>31:
            day=31
        elif select_index==4:
         
          hour+=1
          if hour>23:
            hour=23
        elif select_index==5:
      
          min+=1
          if min>59:
            min=59
        elif select_index==6:
       
          sec+=1
          if sec>59:
            sec=59
        elif select_index==7:
        
          if on_off=='off':
            on_off='on'
          else:
            on_off='off'
        disdate(ssd,year,mon,day,hour,min,sec,on_off)
        time.sleep_ms(200)
        
      if keyvalue==key.HOME_PRESS:
        ssd.rect(select_x,select_y,select_w,select_h,0)
        ssd.show()
        select_index+=1
        if select_index>7:
          select_index=1
        time.sleep_ms(200)
      
      if keyvalue==key.BACK_PRESS:
        data={'alarm':{'on_off':on_off,'year':year,'mon':mon,'day':day,'hour':hour,'min':min,'sec':sec}}
        config.set(self.path,data)
        print(data)
        break


















