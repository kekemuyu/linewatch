




import math
import hzk
import framebuf

def arc(ssd,x,y,r,rad,len,col):
  start=round(rad*100)
  end=round((rad+len)*100)
  for v in range(start,end):
    ssd.pixel(x+round(r*(math.sin(v/100))),y+round(r*(math.cos(v/100))),col)
  ssd.show()
  
def rtriangle(ssd,x,y,r,rad,col):
  x=x+round(r*(math.sin(rad)))
  y=y+round(r*(math.cos(rad)))
  
  x1=x+round(5*(math.sin(-math.pi/2+rad)))
  y1=y+round(5*(math.cos(-math.pi/2+rad)))
  
  x2=x+round(5*(math.sin(0+rad)))
  y2=y+round(5*(math.cos(0+rad)))
  
  x3=x+round(5*(math.sin(math.pi/2+rad)))
  y3=y+round(5*(math.cos(math.pi/2+rad)))

   
  ssd.line(x1,y1,x2,y2,1)
  ssd.line(x1,y1,x3,y3,1)
  ssd.line(x2,y2,x3,y3,1)


def rline(ssd,x1,y1,x2,y2,r,rad,col):
  pass
def rletter_n(ssd,x,y,r,rad,col):
  x=x+round(r*math.sin(rad))
  y=y+round(r*math.cos(rad))
  
  x1=x+round(4*(math.sin(math.pi/4+rad)))
  y1=y+round(4*(math.cos(math.pi/4+rad)))
  
  x2=x+round(4*(math.sin(-math.pi*5/4+rad)))
  y2=y+round(4*(math.cos(-math.pi*5/4+rad)))
  
  x3=x+round(4*(math.sin(-math.pi*3/4+rad)))
  y3=y+round(4*(math.cos(-math.pi*3/4+rad)))
  
  x4=x+round(4*(math.sin(-math.pi/4+rad)))
  y4=y+round(4*(math.cos(-math.pi/4+rad)))
  
  ssd.line(x1,y1,x2,y2,col)
  ssd.line(x1,y1,x3,y3,col)
  ssd.line(x4,y4,x3,y3,col)


def rletter_s(ssd,x,y,r,rad,col):
  x=x+round(r*math.sin(rad))
  y=y+round(r*math.cos(rad))
  
  letter_rad=math.pi/2+rad
  x1=x+round(4*(math.sin(letter_rad)))
  y1=y+round(4*(math.cos(letter_rad)))
  
  x2=x+round(4*(math.sin(math.pi/4+letter_rad)))
  y2=y+round(4*(math.cos(math.pi/4+letter_rad)))
  
  x3=x+round(4*(math.sin(math.pi*3/4+letter_rad)))
  y3=y+round(4*(math.cos(math.pi*3/4+letter_rad)))
  
  x4=x+round(4*(math.sin(math.pi+letter_rad)))
  y4=y+round(4*(math.cos(math.pi+letter_rad)))
  
  x5=x+round(4*(math.sin(math.pi*5/4+letter_rad)))
  y5=y+round(4*(math.cos(math.pi*5/4+letter_rad)))
  
  x6=x+round(4*(math.sin(math.pi*7/4+letter_rad)))
  y6=y+round(4*(math.cos(math.pi*7/4+letter_rad)))
  
  ssd.line(x3,y3,x2,y2,col)
  ssd.line(x4,y4,x1,y1,col)
  ssd.line(x5,y5,x6,y6,col)
  
  ssd.line(x3,y3,x4,y4,col)
  ssd.line(x1,y1,x6,y6,col)
def rletter_w(ssd,x,y,r,rad,col):
  x=x+round(r*math.sin(rad))
  y=y+round(r*math.cos(rad))

  letter_rad=math.pi*3/2+rad
  #letter_r=4
  
  x1=x+round(4*(math.sin(math.pi/4+letter_rad)))
  y1=y+round(4*(math.cos(math.pi/4+letter_rad)))
  
  x2=x+round(4*(math.sin(math.pi*3/4+letter_rad)))
  y2=y+round(4*(math.cos(math.pi*3/4+letter_rad)))
  
  x3=x+round(4*(math.sin(math.pi*5/4+letter_rad)))
  y3=y+round(4*(math.cos(math.pi*5/4+letter_rad)))
  
  x4=x+round(4*(math.sin(math.pi*7/4+letter_rad)))
  y4=y+round(4*(math.cos(math.pi*7/4+letter_rad)))
  
  ssd.line(x2,y2,x3,y3,col)
  ssd.line(x1,y1,x4,y4,col)
  ssd.line(x,y,x3,y3,col)
  ssd.line(x,y,x4,y4,col)
  
  
def rletter_e(ssd,x,y,r,rad,col):
  x=x+round(r*math.sin(rad))
  y=y+round(r*math.cos(rad))

  letter_rad=rad-math.pi/2
  #letter_r=4
  
  x1=x+round(3*(math.sin(letter_rad)))
  y1=y+round(3*(math.cos(letter_rad)))
  
  x2=x+round(4*(math.sin(math.pi/4+letter_rad)))
  y2=y+round(4*(math.cos(math.pi/4+letter_rad)))
  
  x3=x+round(4*(math.sin(math.pi*3/4+letter_rad)))
  y3=y+round(4*(math.cos(math.pi*3/4+letter_rad)))
  
  x4=x+round(3*(math.sin(math.pi+letter_rad)))
  y4=y+round(3*(math.cos(math.pi+letter_rad)))
  
  x5=x+round(4*(math.sin(math.pi*5/4+letter_rad)))
  y5=y+round(4*(math.cos(math.pi*5/4+letter_rad)))
  
  x6=x+round(4*(math.sin(math.pi*7/4+letter_rad)))
  y6=y+round(4*(math.cos(math.pi*7/4+letter_rad)))
  
  ssd.line(x2,y2,x3,y3,col)
  ssd.line(x1,y1,x4,y4,col)
  ssd.line(x5,y5,x6,y6,col)
  ssd.line(x3,y3,x5,y5,col)
  
def circle(ssd,x,y,r,col):
  intpi=round(math.pi*100)
  for v in range(-intpi,intpi):
    ssd.pixel(x+round(r*(math.sin(v/100))),y+round(r*(math.cos(v/100))),col)
def fill_circle(ssd,x,y,r,col):
  for v in range(r):
    circle(ssd,x,y,v,1)
    
def disUnicode(ssd,x,y,str):
  zkpath='unicode.bin'
  hzkpath='gbk.font'
  
  xx=x
  for v in str:
    if ord(v)>128:
      gbkcode=hzk.uni2gbk(ord(v),zkpath)
      arr=hzk.getHZK(gbkcode,hzkpath)
      if arr!=0:
        fbuf = framebuf.FrameBuffer(arr, 16, 16, framebuf.MONO_HLSB)
        ssd.blit(fbuf, xx, y)       
        xx=xx+16
    else:
      ssd.text(v,xx,y+8)  
      xx=xx+8

def slidebar(ssd,x,y,w,h,on_off):

  ssd.fill_rect(x,y,w,h,0)    #clear slidebar
  r=h//2
  if on_off:
    ssd.fill_rect(x,y,w,h,1)
    cx=x+w-r
    cy=y+r
    circle(ssd,cx,cy,r-2,0)
  else:
    ssd.rect(x,y,w,h,1)
    cx=x+r
    cy=y+r
    circle(ssd,cx,cy,r-2,1)
    
def radio(ssd,x,y,str,on_off):
  w=0
  for v in str:
    if ord(v)<=128:
      w+=8
    else:
      w+=16
  
  ssd.fill_rect(x,y,w+16+4,16,0)
  disUnicode(ssd,x,y,str)
  if on_off:
    fill_circle(ssd,x+w+12,y+8,5,1)
  else:
    circle(ssd,x+w+12,y+8,5,1)
  