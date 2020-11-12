

import math
import time
import graph
from machine import I2C,Pin
from qmc5883 import QMC5883
from lis3dh import LIS3DH_I2C

def getDegrees(qmc5883):
  x, y,z,temp = qmc5883.read_scaled()
  print (x, y, z,  temp)
  
  heading=math.atan2(y,x)


  # Convert to degrees
  headingDegrees =180-heading * 180/math.pi;  #芯片的y轴朝向，字面在上是+180，向下是180-
  if headingDegrees<0:
    headingDegrees+=360
  
  return heading,headingDegrees
def getAcceler(acc):
  x=acc.acceleration.x
  y=acc.acceleration.y
  z=acc.acceleration.z
  
  pitch=math.atan2(x,math.sqrt(y*y+z*z))
  roll=math.atan2(y,math.sqrt(x*x+z*z))
  anglez=math.atan2(z,math.sqrt(y*y+x*x))*180/math.pi
  return pitch,roll,anglez
  
def dis_acceler(ssd,pitch,roll,anglez):
  ssd.fill(0)
  ssd.text(str(round(90+anglez)),95,31)
  ssd.pixel(63,31,1)
  
  graph.circle(ssd,63+round(pitch*20),31+round(roll*20),5,1)
  graph.circle(ssd,63,31,24,1)
  ssd.show()
def dis_compass(ssd,heading,degree):
  ssd.fill(0)
  ssd.text(str(round(degree)),51,27)
  graph.circle(ssd,63,31,24,1)
  graph.circle(ssd,63,31,13,1)
  
  
  graph.rletter_n(ssd,63,32,18,-heading,1)
  graph.rletter_s(ssd,63,32,18,-heading+math.pi,1)
  graph.rletter_w(ssd,63,32,18,-heading+math.pi/2,1)
  graph.rletter_e(ssd,63,32,18,-heading-math.pi/2,1)
  
  graph.rtriangle(ssd,63,31,26,-heading,1)
  
  ssd.show()
  #graph.rletter_n(ssd,60,28,19,heading,1)
class Compass:
  COMPASS =0
  ACC =1
  def __init__(self,ssd,key):
    i2c=I2C(1, scl=Pin(5), sda=Pin(4), freq=400000)
    self.qmc5883 = QMC5883(i2c)
    self.acc=LIS3DH_I2C(i2c)
    self.ssd=ssd
    self.key=key
    self.mode=self.COMPASS
  def run(self):
    while True:
      keyvalue=self.key.read()
      if keyvalue==self.key.LEFT_PRESS or keyvalue==self.key.RIGHT_PRESS:
        if self.mode==self.COMPASS:
          self.mode=self.ACC
        elif self.mode==self.ACC:
          self.mode=self.COMPASS
        time.sleep_ms(200)
      if self.mode==self.COMPASS:
        heading,degree=getDegrees(self.qmc5883)
        dis_compass(self.ssd,heading,degree)
      else:
        pitch,roll,anglez=getAcceler(self.acc)
        dis_acceler(self.ssd,pitch,roll,anglez)
  

      if self.key.read()==self.key.BACK_PRESS:
        break

