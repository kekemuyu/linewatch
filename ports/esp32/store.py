







import time
import framebuf
from font import Font 
import os
import config
import wget
import wifi
import extracttar
import gc
import graph

def List(ssd,data,index):
  ssd.fill(0)
  data_len=len(data)
  if data_len<=0:
    return
  

  group_len=data_len//4+1
  group_index=index//4
  screen_index=index%4
    
  screen_len=4

  if group_index==group_len-1:
    screen_len=data_len-group_index*4
  
  #print(index,group_index,screen_index,screen_len)

  
  screen_index_arr=range(screen_len)
  for i in screen_index_arr:
    ssd.text(data[group_index*4+i],20,10+10*i)
    
  ssd.fill_rect(0,0,20,64,0)   #clear ->
  ssd.text('->',0,10*(screen_index+1))
  ssd.show()
  
  
def Showbox(ssd,text,delay):
  ssd.fill(0)
  #ssd.text(text,0,10)
  graph.disUnicode(ssd,0,10,text)
  ssd.show()
  time.sleep(delay)
  
class Myapp:
  def __init__(self,ssd,key,jsonfile):
    self.ssd=ssd
    self.key=key
    self.jsonfile=jsonfile
    
    self.config=config.get(self.jsonfile)
    self.app_dir=self.config['appstore']['myapp_dir']

   
  def run(self):
    key=self.key
    ssd=self.ssd
    
    index=0
    
    data=os.listdir(self.app_dir)
    list_len=len(data)
    
    while True:
      List(ssd,data,index)   
      keyvalue=key.read()
      time.sleep_ms(200)
           
      if keyvalue==key.BACK_PRESS:
        time.sleep_ms(200)
        break
       
      if keyvalue==key.LEFT_PRESS:
        index-=1
        if index<=0:
          index=0
        time.sleep_ms(200)
      if keyvalue==key.RIGHT_PRESS:
        index+=1
        if index>=list_len:
          index=list_len
        time.sleep_ms(200)
      if keyvalue==key.HOME_PRESS:
        exec(open(self.app_dir+data[index]+'/'+data[index]+'.py').read(),globals())
        gc.collect()
        time.sleep_ms(200)
 
 
class Mystore:
  def __init__(self,ssd,key,jsonfile):
    self.ssd=ssd
    self.key=key    

    self.config=config.get(jsonfile)
    self.appurl=self.config['appstore']['app_url']
    listurl=self.config['appstore']['list_url']
    self.list_dir=wget.listdir(listurl)
    if self.list_dir!=None:
      self.store_dir=self.config['appstore']['store_dir']
      self.app_dir=self.config['appstore']['myapp_dir']
      print(self.list_dir,self.store_dir,self.app_dir)
  def run(self):  
    ssd=self.ssd
    key=self.key
 
    index=0
    list_len=len(self.list_dir)
    data=list(self.list_dir.keys())

    while True:
      List(ssd,data,index)    
      
      keyvalue=key.read()
      if keyvalue==key.BACK_PRESS:
        time.sleep_ms(200)
        break
          
      if keyvalue==key.LEFT_PRESS:
        index-=1
        if index<=0:
          index=0
        time.sleep_ms(200)
      if keyvalue==key.RIGHT_PRESS:
        index+=1
        if index>=list_len:
          index=list_len
        time.sleep_ms(200)
      if keyvalue==key.HOME_PRESS:
        download_url=self.appurl+self.list_dir[data[index]]
        print(download_url)
        wget.download(download_url,self.store_dir+data[index])
        extracttar.run(self.store_dir+data[index],self.app_dir)
        gc.collect()
        time.sleep_ms(200)
class Appstore:
  def __init__(self,ssd,key,jsonfile):
    self.ssd=ssd
    self.key=key
    self.jsonfile=jsonfile
    
 
  def run(self):
    ssd=self.ssd
    key=self.key
    menu_index=1
    ssd.fill(0)
    graph.disUnicode(ssd,20,10,'我的应用')
    graph.disUnicode(ssd,20,30,'应用市场')
    #ssd.text('1.my apps',20,10)

    #ssd.text('2.app store',20,20)
    ssd.show()
    time.sleep_ms(200)
   # data=['1.my apps','2.app store']
    while True:
      keyvalue=key.read()

      #List(ssd,data,index)  
      if keyvalue==key.BACK_PRESS:
        break
        
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

        ssd.text('->',0,15)
        ssd.show()
      elif menu_index==2:
        ssd.fill_rect(0,0,20,64,0)
        ssd.text('->',0,35)
        ssd.show()
      
      if keyvalue==key.HOME_PRESS:
        print(menu_index)
        if menu_index==1:
          myapp=Myapp(ssd,key,self.jsonfile) 
          myapp.run() 
  
        if menu_index==2:  
          if wifi.sta.isconnected():
            Showbox(ssd,'获取数据中...',3)
            mystore=Mystore(ssd,key,self.jsonfile)
            
            if mystore.list_dir!=None:
              mystore.run()
            else:
              print('no data')
              Showbox(ssd,'获取数据失败!',3)
          else:
            print('no wifi')
            Showbox(ssd,'没有无线网络!',3)
            
        
        ssd.fill(0)
        graph.disUnicode(ssd,20,10,'我的应用')
        graph.disUnicode(ssd,20,30,'应用市场')

        ssd.show()
        print("clear")
        time.sleep_ms(200)













