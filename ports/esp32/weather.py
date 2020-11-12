








import framebuf
import machine
import time
import config
import font2
import wifi
import graph
import wget

def read(url):
  res=wget.get(url)
  if res==None:
    return None
  return res.json()
  


def disZHString(ssd,data,x,y):
  icon_keys=font2.hanzi_16x16.keys()
  for k,v in enumerate(data):
    if v in icon_keys:
      fbuf = framebuf.FrameBuffer(bytearray(font2.hanzi_16x16[v]), 16, 16, framebuf.MONO_HLSB)
      ssd.blit(fbuf, x+16*k, y)



def disWeather_icon(ssd,data,x,y):

  font_data=''
  if '晴' in data:
    font_data=font2.weather_icon['晴']
  elif '云' in data: 


    font_data=font2.weather_icon['云']
  elif '雨' in data:
    font_data=font2.weather_icon['雨']
  elif '阴' in data:
    font_data=font2.weather_icon['阴']
  elif '雾' in data:
    font_data=font2.weather_icon['雾']
  elif '霾' in data:
    font_data=font2.weather_icon['雾']
  elif '雪' in data:
    font_data=font2.weather_icon['雪']  
  if font_data=='':
    return
  fbuf = framebuf.FrameBuffer(bytearray(font_data), 32, 32, framebuf.MONO_HLSB)
  ssd.blit(fbuf, x, y)  
  
class Weather:
  def __init__(self,ssd,key,jsonfile):
    self.path=jsonfile
    self.ssd=ssd
    self.key=key
  def run(self):
    if  not wifi.sta.isconnected():
      self.ssd.text('wifi is disconnected',10,24)
      return
    conf=config.get(self.path)
    #self.ssd.text('geting data...',10,24)


    graph.disUnicode(self.ssd,10,24,'获取数据...')
    self.ssd.show()

    self.data=read(conf['weatherurl'])
    if self.data!=None:
      self.data=self.data['data']
      print(self.data)
    else:
      graph.disUnicode(self.ssd,10,24,'获取数据失败')
      self.ssd.show()
      time.sleep(2)
      return
    self.ssd.fill(0)
    while True:
      data=self.data
      #self.ssd.text(data['City'],0,5)
     
      self.ssd.text(data['Temp'][:2],30,55)
      fbuf = framebuf.FrameBuffer(bytearray(font2.degree_8x8), 8, 8, framebuf.MONO_HLSB)
      self.ssd.blit(fbuf, 48,55)
      #self.ssd.text(data['Wind'],0,25)
      #self.ssd.text(data['Data'],0,35)
     
      disWeather_icon(self.ssd,data['Data'],44,6)
      graph.disUnicode(self.ssd,80,14,data['Data'])
      #disZHString(self.ssd,data['Data'],80,14)
      self.ssd.line(0,45,127,45,1)
      #self.ssd.text(data['AirLevel'],0,45)
      #self.ssd.text(data['Imgurl'],0,55)
      humidity=data['Humidity']
      humidity=humidity[len(humidity)-3:]
      self.ssd.text(humidity,80,55)
      self.ssd.show()

      
      if self.key.read()==self.key.BACK_PRESS:
        break



















