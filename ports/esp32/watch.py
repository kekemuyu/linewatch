




import config

from key import Key
from machine import Timer,Pin
import time

from menu import Menu

from oled import Oled
from clock import Clock
from sysset import Sysset

from alarm import Alarm

from weather import Weather

import esp32 

import machine 
from store import Appstore
from compass import Compass

jsonfile='./config.json'

class Watch:

  def run():
    oled = Oled(12,2,15,14,13,4)
    ssd=oled.ssd

    #home=14, left=13  right=11 back=7

    key=Key(33,25,26,32)
    key.start()


    keyvalue=15
    
    
    menu_index=1
    menu=Menu(ssd,jsonfile)

    def lowpower(ssd):
      ssd.poweroff()
      machine.deepsleep()
      
    wake1 = Pin(33, mode = Pin.IN)

    #level parameter can be: esp32.WAKEUP_ANY_HIGH or esp32.WAKEUP_ALL_LOW

    esp32.wake_on_ext0(pin = wake1, level = esp32.WAKEUP_ALL_LOW)
    time_cnt=0

    
    clock=Clock(ssd,key)
    alarm=Alarm(ssd,key,jsonfile)
    compass=Compass(ssd,key)
    weather=Weather(ssd,key,jsonfile)
    appstore=Appstore(ssd,key,jsonfile) 
    sysset=Sysset(ssd,key,jsonfile)
    menu_dic={1:menu.clock,2:menu.alarm,3:menu.compass,4:menu.weather,5:menu.appstore,6:menu.sysset}
    menu_event={1:clock.run,2:alarm.run,3:compass.run,4:weather.run,5:appstore.run,6:sysset.run}
    while True:
     # time.sleep_ms(200)
      
      #time_cnt+=1
      #if time_cnt>50:
      #  lowpower(ssd)
      if key.read()==key.LEFT_PRESS:
    
        time_cnt=0
        menu_index=menu_index-1
        if menu_index<=1:
          menu_index=1 
        time.sleep_ms(200)
      elif key.read()==key.RIGHT_PRESS:
   
        time_cnt=0
        menu_index=menu_index+1
        if menu_index>=6:
          menu_index=6
        time.sleep_ms(200)

      
      menu.disSensor(90,0,0.57)
      
      menu_dic[menu_index]()

      if key.read()==key.HOME_PRESS:
        time_cnt=0
        ssd.fill(0)
        menu_event[menu_index]()
        ssd.fill(0)
        time.sleep_ms(200)
if __name__ == '__main__':  
  Watch.run()





