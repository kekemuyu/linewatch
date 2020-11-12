









import wifi
import usocket as socket
import ustruct as struct
import utime 
from machine import RTC


NTP_DELTA = 3155673600
 
host = "cn.pool.ntp.org"  #国内的NTP时间服务器
 
wlan=None
s=None

def time():
  NTP_QUERY = bytearray(48)
  NTP_QUERY[0] = 0x1b
  
  if not wifi.sta.isconnected():
    print('not connected')
    return 0
  if not wifi.sta.active():
    print('not active')
    return 0
  print(socket.getaddrinfo(host, 123))
  addr = socket.getaddrinfo(host, 123)[0][-1]
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.settimeout(5)
  s.sendto(NTP_QUERY, addr)
  msg = s.recv(48)
  print(msg[40:44])
  s.close()
  val = struct.unpack("!I", msg[40:44])[0]
  return val - NTP_DELTA
   
def syncTime():
  t = time()
  if t==0:
    return 0
  t+=3600*8
  tm = utime.localtime(t)
  tm = tm[0:3] + (0,) + tm[3:6] + (0,)
  print(tm)
  year=tm[0]
  print(year)
  month=tm[1]
  day=tm[2]
  hour=tm[4]
  second=tm[6]
  min=tm[5]

  print(month)
  print(day)
  print(hour)
  print(min)
  print(second)
  
  rtc = RTC() 
  rtc.init((year,month,day,2,hour,min,second,0))
  return 1
  '''
if __name__=='__main__':
  t = time()
  print(t)
  tm = utime.localtime(t)
  tm = tm[0:3] + (0,) + tm[3:6] + (0,)
  print(tm)
  year=tm[0]


  print(year)








  month=tm[1]








  day=tm[2]








  hour=tm[4]








  second=tm[6]








  if 16<=hour<24:  #ntp授时获取的是格林尼治时间 这里8区的时间








    day=day+1








  hour=hour+8








  min=tm[5]








  if hour>=24:


    hour=hour-24
  print(month)
  print(day)
  print(hour)
  print(min)
  print(second)
  
  rtc = RTC() 

  rtc.init((year,month,day,2,hour,min,second,0))

'''