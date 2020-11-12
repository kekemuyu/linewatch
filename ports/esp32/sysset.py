



import config
import wifi
import time
import framebuf
from font import Font 
import socket
import json
import synctime 
import graph


class Apopen:
  def run(ssd,key,jsonfile): 
    apinfo=config.get(jsonfile)['apinfo']
    print(apinfo)
    print(apinfo['name'])
    if not wifi.ap.isconnected():
      wifi.ap.config(essid=apinfo['name'])
      wifi.ap.active(True)
   
    ssd.fill(0) 
    graph.disUnicode(ssd,0,0,'打开微信小程序')
    graph.disUnicode(ssd,32,20,'IOT管家')
    
    #ssd.text('essid:'+apinfo['name'],0,40) 
    '''
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[8]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, 0, 10)

    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[7]), 32, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, 31, 10)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[9]), 16, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, 63, 10)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[10]), 16, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, 79, 10)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[11]), 16, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, 95, 10)
    fbuf = framebuf.FrameBuffer(bytearray(Font.hanzi[10]), 16, 32, framebuf.MONO_HLSB)
    ssd.blit(fbuf, 111, 10)
    '''
    ssd.text('ip:'+apinfo['server_ip'],0,40) 
    ssd.text('port:'+str(apinfo['server_port']),0,50) 
    ssd.show()
    
    
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addres=socket.getaddrinfo(apinfo['server_ip'],apinfo['server_port'])[0][-1]
    s.bind(addres)  #绑定端口
    while True:
      keyvalue=key.read()
      time.sleep_ms(200)
      print(keyvalue)
      
      data,addr=s.recvfrom(1024)
      data=json.loads(data)
      if len(data)>0:
       print('received:',data,'from',addr) 
       config.set(jsonfile,data)
       ssd.fill(0)
       ssd.text('SUCCESS!',20,20)
       ssd.show()
       s.close()
       wifi.ap.active(False)
       break
      if keyvalue==7:
        s.close()
        wifi.ap.active(False)
        break

def Wificlose(ssd,key):
  wifi.sta_disconnect()
  ssd.fill(0)
  graph.disUnicode(ssd,0,10,'断开连接...')
  #ssd.text('disconnecting...',0,10)
  ssd.show()
  while True:
    keyvalue=key.read()
    time.sleep_ms(200)

    
    if not wifi.sta.isconnected():
      ssd.fill(0)
      #ssd.text('SUCCESS!',0,10)
      graph.disUnicode(ssd,0,10,'断开连接成功')
      break
    if keyvalue==7:
      time.sleep_ms(200)
      break
    
def Wifiopen(ssd,key,essid,passwd):  
  wifi.essid=essid
  wifi.passwd=passwd
  wifi.sta_connect()

  ssd.fill(0)

  #ssd.text('connecting...',0,10)

  graph.disUnicode(ssd,0,10,'连接中...')
  ssd.show()
  while True:
    keyvalue=key.read()
    time.sleep_ms(200)
    
    if wifi.sta.isconnected():
      ssd.fill(0)
      #ssd.text('SUCCESS!',0,10)
      graph.disUnicode(ssd,0,10,'连接成功')
      ssd.show()
      break
    if keyvalue==7:
      time.sleep_ms(200)
      break
      
class Wifilist:
  def __init__(self,jsonfile):
    self.jsonfile=jsonfile
  def run(self,ssd,key):
    ssd.fill(0)
    #ssd.text('1.open',20,10)
    #ssd.text('2.close',20,20)
    graph.disUnicode(ssd,20,5,'打开')

    graph.disUnicode(ssd,20,25,'关闭')
    ssd.show()
    menu_index=1
    essid=config.get(self.jsonfile)['essid']
    passwd=config.get(self.jsonfile)['passwd']
    while True:
      keyvalue=key.read()

      
      if keyvalue==key.LEFT_PRESS:
        menu_index-=1
        if menu_index<1:
          menu_index=1
        time.sleep_ms(200)
      elif keyvalue==key.RIGHT_PRESS:
        menu_index+=1
        if menu_index>2:
          menu_index=2
        time.sleep_ms(200)
      if menu_index==1:
        ssd.fill_rect(0,0,20,64,0)
        ssd.text('->',0,10)
      elif menu_index==2:
        ssd.fill_rect(0,0,20,64,0)
        ssd.text('->',0,30)
      ssd.show()
      
      if keyvalue==key.HOME_PRESS:
        if menu_index==1:
          Wifiopen(ssd,key,essid,passwd)     
          time.sleep_ms(200)
        elif menu_index==2:
          Wificlose(ssd,key)
          time.sleep_ms(200)
        ssd.fill(0)
        graph.disUnicode(ssd,20,5,'打开')
        graph.disUnicode(ssd,20,25,'关闭')
        #ssd.text('1.open',20,10)
        #ssd.text('2.close',20,20)
        ssd.show()
        print("clear")
        time.sleep_ms(200)
      if keyvalue==key.BACK_PRESS:
        break
        

class Sysset:
  def __init__(self,ssd,key,jsonfile):
    self.ssd=ssd
    self.key=key
    self.menu_index=1
    self.select_y=0
    self.jsonfile=jsonfile

  def run(self):
    key=self.key
    ssd=self.ssd
    graph.disUnicode(ssd,20,5,'热点')
    graph.disUnicode(ssd,20,25,'无线网络')
    graph.disUnicode(ssd,20,45,'时间同步')
      
    while True:
      keyvalue=key.read()
      if keyvalue==key.LEFT_PRESS:
        self.menu_index-=1
        if self.menu_index<1:
          self.menu_index=1
        time.sleep_ms(200)
      elif keyvalue==key.RIGHT_PRESS:
        self.menu_index+=1
        if self.menu_index>3:
          self.menu_index=3
        time.sleep_ms(200)  
          
      if self.menu_index==1:
        ssd.fill_rect(0,0,20,64,0)
        ssd.text('->',0,10)
      elif self.menu_index==2:
        ssd.fill_rect(0,0,20,64,0)
        ssd.text('->',0,30)
      elif self.menu_index==3:
        ssd.fill_rect(0,0,20,64,0)
        ssd.text('->',0,50)
      

      
      #ssd.text('1.open ap',20,10)
      #ssd.text('2.wifi start',20,20)
      #ssd.text('3 sync date',20,30)
      ssd.show()
      
      if keyvalue==key.HOME_PRESS:
        time.sleep_ms(200)
        if self.menu_index==1:
          Apopen.run(ssd,key,self.jsonfile)   
          time.sleep_ms(200)
          ssd.fill(0)
          graph.disUnicode(ssd,20,5,'热点')
          graph.disUnicode(ssd,20,25,'无线网络')
          graph.disUnicode(ssd,20,45,'时间同步')
        elif self.menu_index==2:
          wifilist=Wifilist(self.jsonfile)
          wifilist.run(ssd,key)
          time.sleep_ms(200)
          ssd.fill(0)
          graph.disUnicode(ssd,20,5,'热点')
          graph.disUnicode(ssd,20,25,'无线网络')
          graph.disUnicode(ssd,20,45,'时间同步') 
        elif self.menu_index==3:
          re=synctime.syncTime()
          print(re)
          ssd.fill(0)
          if re==1:
            graph.disUnicode(ssd,0,5,'同步完成')
          else:
            graph.disUnicode(ssd,10,5,'同步失败!')
            graph.disUnicode(ssd,10,25,'没有线网络')      
            ssd.show()
          time.sleep(3)
          ssd.fill(0)
          graph.disUnicode(ssd,20,5,'热点')
          graph.disUnicode(ssd,20,25,'无线网络')
          graph.disUnicode(ssd,20,45,'时间同步')
        
      if keyvalue==key.BACK_PRESS:
        break