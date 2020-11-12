


from machine import Pin,Timer,PWM,RTC
import time
import config


BEEP_PIN = const( 9 )
def didi():
  beeper = PWM(Pin(BEEP_PIN, Pin.OUT), freq=589, duty=512)
  beeper.freq(589)
  time.sleep_ms(100)
  
  beeper.freq(0)
  time.sleep_ms(50)
  
  beeper.freq(589)
  time.sleep_ms(100)
  
  beeper.freq(0)
  time.sleep_ms(650)
  beeper.deinit()
class Beep:

  
  def __init__(self,key,n,json_path):      
    self.n = n
    self.tim1=Timer(1)
    self.cnt=0
    self.beep_start=False
    self.beeper=None
    self.freq589_on=False
    self.freq0_on=False
    self.key=key
    self.path=json_path
  def run(self):
    self.stop()
    
    alarm=config.get(self.path)['alarm']
    
    alarm_year=alarm['year']
    alarm_mon=alarm['mon']
    alarm_day=alarm['day']
    
    alarm_hour=alarm['hour']

    alarm_min=alarm['min']
    alarm_sec=alarm['sec']
        
    alarm_on_off=alarm['on_off']
    if alarm_on_off=='on':
      rtc=RTC()  


      dt=rtc.datetime()
    
      year=dt[0]
      mon=dt[1]
      day=dt[2]   
      hour=dt[4]
      min=dt[5]
      sec=dt[6]
      
      if hour==alarm_hour and min==alarm_min and sec==alarm_sec and self.beep_start==False:  
        self.beeper = PWM(Pin(self.BEEP_PIN, Pin.OUT), freq=589, duty=512)
        self.beep_start=True

      
      if self.beep_start and self.n>=0:
        self.n-=1
        self.beeper.freq(589)
        time.sleep_ms(100)
        
        self.beeper.freq(0)
        time.sleep_ms(50)
        
        self.beeper.freq(589)
        time.sleep_ms(100)
        
        self.beeper.freq(0)
        time.sleep_ms(650)
          
      if (self.beep_start and self.n<=0) or (self.key.read()==self.key.HOME_PRESS and self.beep_start):
        self.cnt=0
        self.freq0_on=False
        self.freq589_on=False
        self.beep_start=False
        self.beeper.deinit()
    self.start()
  
  def start(self):
    self.tim1.init(period=100,mode=Timer.PERIODIC,callback=lambda t:self.run())
  def stop(self):
    self.tim1.deinit()
   




