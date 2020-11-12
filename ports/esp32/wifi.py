


import network

sta=network.WLAN(network.STA_IF)
ap=network.WLAN(network.AP_IF)

essid=''
passwd=''

def sta_connect():
  sta.active(True)
  sta.connect(essid,passwd)

def sta_disconnect():
  sta.disconnect()
  sta.active(False)  
  




