import glob
import os

for f in glob.glob('downsampled/*.jpg'):
  new_filename = f.replace("_downsampled", "")
  os.rename(f,new_filename)
