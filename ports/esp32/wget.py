


try:
    import urequests as requests
except ImportError:
    import requests
import ure    


def listdir(url):
  try:
     r=requests.get(url)
  except Exception as e:
    return None
 
  str=r.json()
  outstr={}
  for v in str['data']:
    name=v[v.rindex('/')+1:]
    outstr[name]=v
  return outstr
  
def download(url,path):
  try:
     r=requests.get(url)
  except Exception as e:
    return None
  
  rbytes=r.content
    
  f = open(path,'wb+')
  f.write(rbytes)
  f.close()
  
def get(url):
  try:
     r=requests.get(url)
  except Exception as e:
    return None
  return r
  
'''
    r=requests.get(url+'/'+v)
    rbytes=r.content
    
    f = open(path+'/'+v,'w+')
    f.write(rbytes)
    f.close()

'''
