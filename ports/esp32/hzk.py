
import os
import struct


def uni2gbk(src,zkpath):
  size=os.stat(zkpath)[6]
  fin=open(zkpath,'rb')
  
  hi=size//4-1
  li=0
  
  
  for n in range(16,0,-1):
    i=int(li+(hi-li)/2)
    
    fin.seek(i*4,0)
    buf=fin.read(4)

    re=struct.unpack('<HH',buf)

    if src==re[0]:
      fin.close()
      return re[1]

    if src>re[0]:
      li=i
    else:
      hi=i
    
  fin.close()
  return 0

def getHZK(gbkcode,gbkpath):
  hi=(gbkcode&0xFF00)>>8
  li=gbkcode&0xFF
  
  pos=((hi-0x81)*191+(li-0x40))*32
  
  fin=open(gbkpath,'rb')
  fin.seek(pos)
  buf=bytearray(32)
  fin.readinto(buf)
  fin.close
  
  return buf




