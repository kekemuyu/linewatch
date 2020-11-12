

import sys
import os
import shutil
import utarfile
import time



def run(src,dest_dir):
  t = utarfile.TarFile(src)
  prefix=dest_dir
  for i in t:
    i.name=i.name.rstrip('/')
    print(i,i.name)
    i.name=prefix+i.name
    print(i.name)
    if i.type == utarfile.DIRTYPE:
      try:
        os.mkdir(i.name)
      except OSError as e:
        if e.args[0] != errno.EEXIST and e.args[0] != errno.EISDIR:
          raise e
     
    else:
      f = t.extractfile(i)
      print(i.name)
      shutil.copyfileobj(f, open(i.name, "wb+"))


