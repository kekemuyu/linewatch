


import json

def set(filename,data): 
  re=get(filename)
  re.update(data)
  f=open(filename, 'w+')
  f.write(json.dumps(re))
  f.close()
  
def get(filename):
  f = open(filename, 'r')
  c = json.loads(f.read())
  f.close()
  return c









